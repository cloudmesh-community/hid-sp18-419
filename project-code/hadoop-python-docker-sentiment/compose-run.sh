#!/bin/bash

DESTDIR=Results

docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
echo "build the cluster"
docker-compose build
echo "DONE"

echo "starting the containers..."
docker-compose up -d
echo "http://localhost:8088 for YARN"

echo "running the sentiment analysis on movie reviews..."
docker exec master /etc/runall.sh

echo "getting the results..."
rm -rf $DESTDIR
mkdir $DESTDIR
docker cp master:/cloudmesh/python/output_pos_tagged ./$DESTDIR
docker cp master:/cloudmesh/python/output_neg_tagged ./$DESTDIR
docker cp master:/cloudmesh/python/log.txt ./$DESTDIR
cp docker-compose.yml ./$DESTDIR