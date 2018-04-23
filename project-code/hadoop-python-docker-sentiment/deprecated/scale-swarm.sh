#!/bin/bash

if [ $1 == "1" ]; then
	echo "docker-compose.yml created with #worker 1"
    cp ./docker-compose-template-swarm.yml ./docker-swarm.yml
    exit 0
fi

cp ./docker-compose-template-swarm.yml ./docker-swarm.yml
for i in $(seq 2 $1)
do
printf "  worker"$i":\n\
    image: minchen57/hadoop-docker-python-sentiment-compose-worker\n\
    ports:\n\
      - \"$((9900+$i)):9864\"\n\
      - \"$((8040+$i)):8042\"\n\n"\
>>./docker-swarm.yml
done
echo "docker-compose.yml created with #worker "$1
exit 0
