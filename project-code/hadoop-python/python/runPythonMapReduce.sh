#!/bin/bash

# split data

cd /cloudmesh/python/data
./split_data.sh

# run

export PATH=$PATH:/$HADOOP_PREFIX/bin
export JARFILE=$HADOOP_PREFIX/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar

# load data
cd /cloudmesh/python
hadoop fs -mkdir training_pos training_neg testing_pos testing_neg
hadoop fs -put ./data/train/pos/* training_pos
hadoop fs -put ./data/train/neg/* training_neg
hadoop fs -put ./data/test/pos/* testing_pos
hadoop fs -put ./data/test/neg/* testing_neg

# training
hadoop  jar $JARFILE \
		-input training_neg \
		-output neg_train   \
		-file /cloudmesh/python/trainingMapper.py  \
		-file /cloudmesh/python/trainingReducer.py \
		-mapper /cloudmesh/python/trainingMapper.py  \
		-reducer /cloudmesh/python/trainingReducer.py 

hadoop  jar $JARFILE \
		-input training_pos \
		-output pos_train   \
		-file /cloudmesh/python/trainingMapper.py  \
		-file /cloudmesh/python/trainingReducer.py \
		-mapper /cloudmesh/python/trainingMapper.py  \
		-reducer /cloudmesh/python/trainingReducer.py		

# get the model
rm -rf pos_train neg_train
hadoop fs -get pos_train
hadoop fs -get neg_train
cp pos_train/part-00000 pos.txt
cp neg_train/part-00000 neg.txt
		

# testing
hadoop  jar $JARFILE \
		 -input testing_pos \
		 -output output_pos_tagged   \
		 -file /cloudmesh/python/pos.txt \
		 -file /cloudmesh/python/neg.txt \
		 -file /cloudmesh/python/testingMapper.py \
		 -file /cloudmesh/python/testingReducer.py\
		 -mapper /cloudmesh/python/testingMapper.py\
		 -reducer /cloudmesh/python/testingReducer.py		

hadoop  jar $JARFILE \
		 -input testing_neg \
		 -output output_neg_tagged   \
		 -file /cloudmesh/python/pos.txt \
		 -file /cloudmesh/python/neg.txt \
		 -file /cloudmesh/python/testingMapper.py \
		 -file /cloudmesh/python/testingReducer.py\
		 -mapper /cloudmesh/python/testingMapper.py\
		 -reducer /cloudmesh/python/testingReducer.py

# results
		
rm -rf output_pos_tagged
rm -rf output_neg_tagged
hadoop fs -get output_pos_tagged
hadoop fs -get output_neg_tagged
		
echo "Sentiment analysis finished execution"
echo "See results in: output_pos_tagged and output_neg_tagged"
echo "In the positive labeled testing files: "
tail -2 output_pos_tagged/part-00000
echo "In the negative labeled testing files: "
tail -2 output_neg_tagged/part-00000
