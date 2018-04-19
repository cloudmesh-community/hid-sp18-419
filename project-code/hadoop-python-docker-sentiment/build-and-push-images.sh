#!/bin/bash

docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
docker build -t minchen57/hadoop-docker-python-sentiment-pseudo:latest hadoop-pseudo

docker push minchen57/hadoop-docker-python-sentiment-compose-base:latest
docker push minchen57/hadoop-docker-python-sentiment-compose-master:latest
docker push minchen57/hadoop-docker-python-sentiment-compose-worker:latest
docker push minchen57/hadoop-docker-python-sentiment-pseudo:latest
