#!/bin/bash

if [ $# -ne 1 ]; then
    ./scale-compose.sh 1
else ./scale-compose.sh $1
fi

./compose-run.sh

docker-compose down
