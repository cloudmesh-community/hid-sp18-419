#!/bin/bash

/etc/bootstrap.sh 2>&1 | tee -a /cloudmesh/python/log.txt
cd /cloudmesh/python
./runPythonMapReduce.sh 2>&1 | tee -a /cloudmesh/python/log.txt