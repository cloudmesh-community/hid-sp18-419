#!/bin/bash

if [ $# -ne 2 ]; then
    echo 1>&2 Usage: [# of iteration][# of workers]
    echo "e.g. 5 3"
    exit -1
fi

worker=$2
cp ./docker-swarm-benchmark-template.yml ./docker-swarm-benchmark.yml
printf "entrypoint: [\"/etc/bootstrap.sh\", \"-benchmark\", \""$1"\",  \""$worker"\"]"\
>>./docker-swarm-benchmark.yml

echo "starting the containers in swarm mode"
docker stack deploy --compose-file docker-swarm-benchmark.yml hadoop-sentiment
echo "scale up the service to $worker worker"
docker service scale hadoop-sentiment_worker=$worker

echo "running the sentiment analysis on movie reviews at backend..."
echo "getting physical node that runs master"
nodeID=$(docker stack ps  -f "name=hadoop-sentiment_master.1" --format "{{.Node}}" hadoop-sentiment)
echo $nodeID
s1=${nodeID: -1}
s2=0
if [ "$s1" == "$s2" ]; then
    echo "Please look for results at: "
    echo "http://149.165.150.80:50070"
    echo "Please track jobs and resources at : "
    echo "http://149.165.150.80:8088/cluster"
else
    echo "Please look for results at: "
    echo "http://149.165.150.7${nodeID: -1}:50070"
    echo "Please track jobs and resources at : "
    echo "http://149.165.150.7${nodeID: -1}:8088/cluster"
fi


