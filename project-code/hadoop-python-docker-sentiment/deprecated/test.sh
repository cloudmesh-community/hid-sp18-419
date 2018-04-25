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

host="http://149.165.150.76"

echo "Please look for results at: "
echo "$host:50070"
echo "Please track jobs and resources at : "
echo "$host:8088/cluster"

until curl -f -s "$host:8088/logs/log.txt";
do
    echo "not yet, please wait"
    sleep 120
done

echo "getting the results..."
rm -rf $DESTDIR
wget -r -nH -np -R "index.html*" "$host:8088/logs"
mv logs/ $DESTDIR/

echo "done"
