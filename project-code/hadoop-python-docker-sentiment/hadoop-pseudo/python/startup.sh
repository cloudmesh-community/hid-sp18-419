#!/bin/bash

/etc/bootstrap.sh 2>&1 | tee -a /cloudmesh/python/log.txt
cd /cloudmesh/python
(time ./runPythonMapReduce.sh) 2>&1 | tee -a /cloudmesh/python/log.txt