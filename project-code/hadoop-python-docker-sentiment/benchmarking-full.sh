#!/bin/bash

if [ $# -ne 2 ]; then
    echo 1>&2 Usage: [# of iteration][# of workers]
    echo "e.g. 5"
    exit -1
fi

worker=$2

DESTDIR=benchmark-full
mkdir -p $DESTDIR

docker network rm hadoop-sentiment
docker network create hadoop-sentiment

echo "Build the image"
docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker

for i in $(seq 1 $1)
do
echo "Worker# =" $2 ", Iter :" $i

echo "starting the containers..."
docker-compose scale master=1 worker=$((worker))

echo "pause for 20 seconds"
sleep 20
echo "Run the container with sentiment analysis on hadoop"
docker exec master /etc/runall.sh

echo "Get the results"
#docker cp pseudo-hadoop:/cloudmesh/python/output_pos_tagged ./$DESTDIR/output_pos_tagged_$TAG
#docker cp pseudo-hadoop:/cloudmesh/python/output_neg_tagged ./$DESTDIR/output_neg_tagged_$TAG
docker cp master:/cloudmesh/python/log.txt ./$DESTDIR/temp.txt

echo "Write the result"
tail -3 ./$DESTDIR/temp.txt |head -1>>./$DESTDIR/$2_worker.txt
rm ./$DESTDIR/temp.txt
echo "Stop the container"
docker-compose down
done

docker network rm hadoop-sentiment




