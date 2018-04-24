#!/bin/bash

export HADOOP_VERSION=2.9.0

# split data

echo "###############################################"
echo "Splitting the training and testing data"
echo "###############################################"

cd /cloudmesh/python/data
./split_data.sh 405409

echo "###############################################"
echo "Data split is done"
echo "###############################################"

# run
export PATH=$PATH:/$HADOOP_PREFIX/bin
export JARFILE=$HADOOP_PREFIX/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar
hdfs dfsadmin -safemode leave



# load data
echo "###############################################"
echo "Load data to hdfs"
echo "###############################################"

cd /cloudmesh/python
hadoop fs -mkdir -p /nlp/training_pos /nlp/training_neg /nlp/testing_pos /nlp/testing_neg
hadoop fs -put ./data/train/pos/* /nlp/training_pos
hadoop fs -put ./data/train/neg/* /nlp/training_neg
hadoop fs -put ./data/test/pos/* /nlp/testing_pos
hadoop fs -put ./data/test/neg/* /nlp/testing_neg

echo "###############################################"
echo "Data loaded"
echo "###############################################"

# training

echo "###############################################"
echo "Mapreduce job 1/4: training on negative reviews"
echo "###############################################"

hadoop  jar $JARFILE \
		-input /nlp/training_neg \
		-output /nlp/neg_train   \
		-file /cloudmesh/python/trainingMapper.py  \
		-file /cloudmesh/python/trainingReducer.py \
		-mapper /cloudmesh/python/trainingMapper.py  \
		-reducer /cloudmesh/python/trainingReducer.py 

echo "###############################################"
echo "Mapreduce job 2/4: training on positive reviews"
echo "###############################################"

hadoop  jar $JARFILE \
		-input /nlp/training_pos \
		-output /nlp/pos_train   \
		-file /cloudmesh/python/trainingMapper.py  \
		-file /cloudmesh/python/trainingReducer.py \
		-mapper /cloudmesh/python/trainingMapper.py  \
		-reducer /cloudmesh/python/trainingReducer.py		

# get the model

echo "###############################################"
echo "Get the trained model"
echo "###############################################"

rm -rf pos_train neg_train
hadoop fs -get /nlp/pos_train
hadoop fs -get /nlp/neg_train
cp pos_train/part-00000 pos.txt
cp neg_train/part-00000 neg.txt

echo "###############################################"		
echo "Mapreduce job 3/4: testing on positive reviews"
echo "###############################################"

# testing
hadoop  jar $JARFILE \
		 -input /nlp/testing_pos \
		 -output /nlp/output_pos_tagged   \
		 -file /cloudmesh/python/pos.txt \
		 -file /cloudmesh/python/neg.txt \
		 -file /cloudmesh/python/testingMapper.py \
		 -file /cloudmesh/python/testingReducer.py\
		 -mapper /cloudmesh/python/testingMapper.py\
		 -reducer /cloudmesh/python/testingReducer.py		

echo "###############################################"
echo "Mapreduce job 4/4: testing on negative reviews"
echo "###############################################"

hadoop  jar $JARFILE \
		 -input /nlp/testing_neg \
		 -output /nlp/output_neg_tagged   \
		 -file /cloudmesh/python/pos.txt \
		 -file /cloudmesh/python/neg.txt \
		 -file /cloudmesh/python/testingMapper.py \
		 -file /cloudmesh/python/testingReducer.py\
		 -mapper /cloudmesh/python/testingMapper.py\
		 -reducer /cloudmesh/python/testingReducer.py

# results
		
rm -rf output_pos_tagged
rm -rf output_neg_tagged
hadoop fs -get /nlp/output_pos_tagged
hadoop fs -get /nlp/output_neg_tagged

echo "###############################################"
echo "Sentiment analysis finished execution"
echo "See results in: "
echo "output_pos_tagged and output_neg_tagged"
echo "###############################################"
echo "In the positive labeled testing files: "
tail -2 output_pos_tagged/part-00000
echo "In the negative labeled testing files: "
tail -2 output_neg_tagged/part-00000
echo "###############################################"

