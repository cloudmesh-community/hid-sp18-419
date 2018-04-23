#!/bin/bash

DESTDIR=Results

docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
echo "build the cluster"
echo "DONE"

echo "starting the containers in swarm mode"
docker stack deploy --compose-file docker-swarm.yml hadoop-sentiment
echo "running the sentiment analysis on movie reviews at backend..."

echo "pausing for 20s"
sleep 20
echo "Continuing ...."

echo "getting physical node that runs master"
nodeID=$(docker stack ps  -f "name=hadoop-sentiment_master.1" --format "{{.Node}}" hadoop-sentiment)
echo $nodeID
echo "Please look for results at: "
echo "http://149.165.150.7${nodeID: -1}:50070"
echo "Please track jobs and resources at : "
echo "http://149.165.150.7${nodeID: -1}:8088/cluster"
