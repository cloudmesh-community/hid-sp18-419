#!/bin/bash

if [ $# -ne 1 ]; then
worker=1
else worker=$1
fi

DESTDIR=Results

docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker

echo "create the network"
docker network rm hadoop-sentiment
docker network create hadoop-sentiment


echo "starting the containers..."
docker-compose scale master=1 worker=$((worker))

echo "http://hostname:8088 for YARN"
echo "http://hostname:50070 for HDFS"

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
