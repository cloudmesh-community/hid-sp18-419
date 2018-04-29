#!/bin/bash

if [ $# -ne 1 ]; then
worker=1
else worker=$1
fi

DESTDIR=Results

docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker

docker-compose down
if docker network rm hadoop-sentiment
then
    echo "existing network removed"
else
    echo "no existing network found"
fi

echo "create the network"
docker network create hadoop-sentiment


echo "starting the containers..."
docker-compose scale master=1 worker=$((worker))

echo "http://localhost:8088 for YARN"
echo "http://localhost:50070 for HDFS"
echo "if you are on Echo, use 149.165.150.76 to replace localhost"

echo "pause for 20 seconds"
sleep 20
echo "running the sentiment analysis on movie reviews..."
docker exec master /etc/runall.sh

echo "getting the results..."
rm -rf $DESTDIR
mkdir $DESTDIR
docker cp master:/cloudmesh/python/output_pos_tagged ./$DESTDIR
docker cp master:/cloudmesh/python/output_neg_tagged ./$DESTDIR
docker cp master:/cloudmesh/python/log.txt ./$DESTDIR
cp docker-compose.yml ./$DESTDIR
echo "see results in Results/"

docker-compose down
docker network rm hadoop-sentiment
echo "containers and netowrk removed"
