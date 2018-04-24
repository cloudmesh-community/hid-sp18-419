#!/bin/bash

: ${HADOOP_PREFIX:=/usr/local/hadoop}

$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

rm /tmp/*.pid

# installing libraries if any - (resource urls added comma separated to the ACP system variable)
cd $HADOOP_PREFIX/share/hadoop/common ; for cp in ${ACP//,/ }; do  echo == $cp; curl -LO $cp ; done; cd -

# altering the core-site configuration
#sed s/NAMENODE/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/core-site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml
#sed s/NAMENODE/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/hdfs-site.xml.template > /usr/local/hadoop/etc/hadoop/hdfs-site.xml
#sed s/RESOURCEMANAGER/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/yarn-site.xml.template.template > /usr/local/hadoop/etc/hadoop/yarn-site.xml.template

service sshd start
nohup $HADOOP_PREFIX/bin/hdfs namenode &
nohup $HADOOP_PREFIX/bin/yarn resourcemanager &
nohup $HADOOP_PREFIX/bin/yarn timelineserver &
nohup $HADOOP_PREFIX/bin/mapred historyserver &

mkdir -p $HADOOP_PREFIX/logs
chmod 777 $HADOOP_PREFIX/logs
date > $HADOOP_PREFIX/logs/temp.txt

if [[ $1 == "-d" ]]; then
    while true; do sleep 1000; done
fi

if [[ $1 == "-bash" ]]; then
    /bin/bash
fi

if [[ $1 == "-run" ]]; then
    sleep 45
    (time /cloudmesh/python/runPythonMapReduce.sh) 2>&1 | tee -a /cloudmesh/python/log.txt
    export PATH=$PATH:/$HADOOP_PREFIX/bin
    tail -3 /cloudmesh/python/log.txt |head -1>> /cloudmesh/python/time.txt
    cp /cloudmesh/python/time.txt $HADOOP_PREFIX/logs/time.txt
    cp /cloudmesh/python/log.txt $HADOOP_PREFIX/logs/log.txt
    cp -r /cloudmesh/python/output_pos_tagged $HADOOP_PREFIX/logs/output_pos_tagged
    cp -r /cloudmesh/python/output_neg_tagged $HADOOP_PREFIX/logs/output_neg_tagged
    while true; do sleep 1000; done
fi

#if [[ $1 == "-benchmark" ]]; then
#    sleep 30
#    export PATH=$PATH:/$HADOOP_PREFIX/bin
#    for i in $(seq 1 $2)
#    do
#        hadoop fs -rm -R /nlp
#        (time /cloudmesh/python/runPythonMapReduce.sh) 2>&1 | tee -a /cloudmesh/python/log.txt
#        tail -3 /cloudmesh/python/log.txt |head -1>>/cloudmesh/python/$3_worker.txt
#        mkdir -p $HADOOP_PREFIX/logs
#        chmod 777 $HADOOP_PREFIX/logs
#        cp /cloudmesh/python/log.txt $HADOOP_PREFIX/logs/log.txt
#        cp /cloudmesh/python/$3_worker.txt $HADOOP_PREFIX/logs/$3_worker.txt
#    done
#    while true; do sleep 1000; done
#fi
