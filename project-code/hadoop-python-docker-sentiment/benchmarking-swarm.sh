#!/bin/bash

if [ $# -ne 2 ]; then
    echo 1>&2 Usage: [# of iteration][# of workers]
    echo "e.g. 5"
    exit -1
fi

worker=$2

DESTDIR=benchmark-swarm
mkdir -p $DESTDIR

for i in $(seq 1 $1)
do

    ./swarm-down.sh
    sleep 30
    echo "Worker# =" $worker ", Iter :" $i

    echo "starting the containers in swarm mode"
    if docker stack deploy --compose-file docker-swarm.yml hadoop-sentiment
    then
        echo "services started"
    else
        echo "something is wrong, continue with next iteration"
        continue
    fi

    echo "scale up the service to $worker worker"
    if docker service scale hadoop-sentiment_worker=$worker
    then
        echo "service scaled"
    else
        echo "something is wrong, continue with next iteration"
        continue
    fi

    echo "running the sentiment analysis on movie reviews at backend..."
    echo "getting physical node that runs master"
    nodeID=$(docker stack ps  -f "name=hadoop-sentiment_master.1" --format "{{.Node}}" hadoop-sentiment)
    echo $nodeID
    s1=${nodeID: -1}
    s2=0
    if [ "$s1" == "$s2" ]; then
        host="http://149.165.150.80"
    else
        host="http://149.165.150.7${nodeID: -1}"
    fi
    echo "Please look for results at: "
    echo "$host:50070"
    echo "Please track jobs and resources at : "
    echo "$host:8088/cluster"


    echo "Please wait for results..."
    j=1
    until curl -f -s "$host:8088/logs/log.txt";
    do
        if [[ j -gt 20 ]]; then
            break
        fi
        echo "not yet, please wait"
        sleep 60
        j=$((j+1))
    done

    echo "getting the results..."
    curl "$host:8088/logs/time.txt" >> ./$DESTDIR/$2_worker.txt

done

./swarm-down.sh


