#
# Naturally you need to adapt this to make work for your project
#

all: start run

start:
	/usr/local/hadoop/etc/hadoop/hadoop-env.sh
	/usr/local/hadoop/sbin/start-dfs.sh
	hdfs dfs -mkdir /user
	hdfs dfs -mkdir /user/${USER}

run:
	runall.sh

clean: 
	/usr/local/hadoop/sbin/stop-dfs.sh
	hdfs namenode -format
	rm -R *.txt
	rm -R data/test
	rm -R data/train
	rm -R *train
	rm -R *tagged
