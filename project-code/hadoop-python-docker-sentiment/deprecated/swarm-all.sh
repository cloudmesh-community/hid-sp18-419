#!/bin/bash

if [ $# -ne 1 ]; then
    ./scale-swarm.sh 1
else ./scale-swarm.sh $1
fi

./swarm-run.sh

