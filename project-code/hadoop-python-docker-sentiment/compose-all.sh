#!/bin/bash

./compose-pull-image.sh

if [ $# -ne 1 ]; then
    ./scale.sh 1
else ./scale.sh $1
fi

./compose-run.sh

docker-compose down