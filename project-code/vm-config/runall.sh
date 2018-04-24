#!/bin/bash

# cd /cloudmesh/python
time ./runPythonMapReduce.sh 2>&1 | tee -a log.txt

hadoop fs -put log.txt .
