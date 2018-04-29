# Apache Hadoop 2.9.0 Docker cluster for sentiment analysis on movie reviews

This directory contains running dockerized hadoop clusters with application of sentiment analysis on movie review (Polarity 2.0 data)

Dockerfiles are modified from [sequenceiq/hadoop-docker](https://github.com/sequenceiq/hadoop-docker) and [Lewuathe/docker-hadoop-cluster](https://github.com/Lewuathe/docker-hadoop-cluster)

The author appreciates the help of Bo Feng regarding the cluster deployment on Echo under swarm mode.

## Run fully distributed cluster using the Makefile

* Pre-requisite: Docker, Docker-compose, Make
* Single command to build images, start cluster, run analysis and get back results before shutting down the cluster by providing the number of workers needed (default is 1):

		make all worker=(#OFWORKERS)

	example: 
		make all worker=3

* Build images needed for master and workers

		make build worker=(#OFWORKERS)
		
* Launch hadoop cluster by using docker-compose with interactive shell

		make shell

* Launch hadoop cluster at back end with certain number of workers

		make start worker=(#OFWORKERS)

* Run the analysis after cluster is lunched

		make run

* Get the analysis result

		make get

* Shut down the cluster

		make down
		
* One can check the ResourceManger at [http://localhost:8088](http://localhost:8088) and HDFS at [http://localhost:50070](http://localhost:50070)

## Run pseudo-distributed cluster 

To execute the pseudo-distributed cluster and get results, one could use the shell script:

		./pseudo-run.sh

There is also a Makefile in the directory hadoop-pseudo allowing more options including build image, start cluster, start interactive shell etc. For details, please see the Readme.md file

		vi hadoop-pseudo/Readme.md

## Run cluster on Echo using docker-compose (without swarm mode)

The cluster can be deployed on FutureSystem Echo. Both pseudo-distributed and fully distributed clusters are supported. 

* clone the repository 
		
		git clone https://github.com/cloudmesh-community/hid-sp18-419.git

* cd to the directory hadoop-python-docker-sentiment

		 cd hid-sp18-419/project-code/hadoop-python-docker-sentiment/

* To start pseudo-distributed cluster, run analysis and get back results before shutting down the cluster

		./pseudo-run.sh

* To start fully distributed cluster with number of workers using docker-compose, run analysis and get back results before shutting down the cluster 

		./compose-run.sh (#OFWORKERS)

	example:
		./compose-run.sh 3

* To remove the Results folders

		./clean.sh

* Notice that when the cluster is up and running, one can also use the folloiwng command to scale up or down the size of the cluster (to $N workers) without shutting down the cluster

		docker-compose scale master=1 worker=$N


## Run cluster on Echo using docker stack deploy (with swarm mode)

The cluster can be deployed on FutureSystem Echo under the docker swarm mode. There is no point to run pseudo-distributed cluster here, the following is for fully distributed cluster:

* clone the repository (if you have not done so)
		
		git clone https://github.com/cloudmesh-community/hid-sp18-419.git

* cd to the directory hadoop-python-docker-sentiment

		 cd hid-sp18-419/project-code/hadoop-python-docker-sentiment/

* To start fully distributed cluster with number of workers using docker stack deploy, run analysis and get back the result: 

		./swarm-run.sh (#OFWORKERS)

	example:
		./swarm-run.sh 30
	
* At the end of the previous command, there will be http addresses provided in the terminal such as:

		Please look for results at:
		http://149.165.150.XX:50070
		Please track jobs and resources at : 
		http://149.165.150.XX:8088/cluster

	These addresses could used access the resourcemanager YARN and HDFS, one can view the process of the mapreduce jobs there. 

* To remove the deployed stack after running

		./swarm-down.sh

* Note: due to the complication of different physical nodes, sometimes one node could be pulling images from docker-hub and causing delay in start-up of datanodes thus ignored by the namenode. In extreme case, the web interface at http://149.165.150.XX:8088/cluster will show 0 active node and one need to use ctrl+C to stop the script, remove the stack and rerun the command:
		
		ctrl + c
		./swarm-down.sh
		./swarm-run.sh (#OFWORKERS)


* Similarly, the service could be scaled up or down to $N workers using the following command at any point when the cluster is actually running:

		docker service scale hadoop-sentiment_worker=$N

## Benchmarking running time

Use the two following shell scripts to run customized number of iterations in order to compute average running time. This can be applied to both echo and local environment. 

* Fully distributed cluster with (#OFWORKERS) of workers and (#ITER) iterations (without swarm)

		./benchmarking-full.sh (#ITER) (#OFWORKERS)
		
* Result of each iteration will be written to each line of a text file at

		 ./benchmark-full/(#OFWORKERS)_worker.txt

* Fully distributed cluster with (#OFWORKERS) of workers and (#ITER) iterations (with swarm)

		./benchmarking-swarm.sh (#ITER) (#OFWORKERS)
		
* Result of each iteration will be written to each line of a text file at

		 ./benchmark-swarm/(#OFWORKERS)_worker.txt

* Note: due to the complication of different physical nodes, sometimes one node could cause delay in start-up of datanodes thus ignored by the namenode. In extreme case, the web interface at http://149.165.150.XX:8088/cluster will show 0 active node and the mapreduce job will terminate when it tries to start. The benchmarking script will continue running and ignore the unsuccessful iteration. In case one wants to use ctrl+C to stop the script, remove the stack and rerun the command: 
		
		ctrl + c
		./swarm-down.sh
		./benchmark-swarm.sh (#ITER) (#OFWORKERS)


* Pseudo-distributed cluster with (#ITER) iterations

		./benchmarking-pseudo.sh (#ITER) 
* Result of each iteration will be written to each line of a text file at 

		./benchmark-pseudo/pseudo.txt
