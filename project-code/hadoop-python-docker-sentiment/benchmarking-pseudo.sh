#!/bin/bash

if [ $# -ne 1 ]; then
    echo 1>&2 Usage: [# of iteration]
    echo "e.g. 5"
    exit -1
fi

DESTDIR=benchmark-pseudo
mkdir -p $DESTDIR

echo "Build the image"
docker build -t minchen57/hadoop-docker-python-sentiment-pseudo:latest hadoop-pseudo

for i in $(seq 1 $1)
do
echo "Iter :" $i
echo "Run the container with sentiment analysis on hadoop"
docker run -it --name pseudo-hadoop minchen57/hadoop-docker-python-sentiment-pseudo:latest 

echo "Get the result"
#docker cp pseudo-hadoop:/cloudmesh/python/output_pos_tagged ./$DESTDIR/output_pos_tagged_$TAG
#docker cp pseudo-hadoop:/cloudmesh/python/output_neg_tagged ./$DESTDIR/output_neg_tagged_$TAG
docker cp pseudo-hadoop:/cloudmesh/python/log.txt ./$DESTDIR/temp.txt

echo "Write the result"
tail -3 ./$DESTDIR/temp.txt |head -1>>./$DESTDIR/pseudo.txt
rm ./$DESTDIR/temp.txt
echo "Stop the container"
docker stop pseudo-hadoop
docker rm pseudo-hadoop
done




