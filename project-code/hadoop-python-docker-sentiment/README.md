# Apache Hadoop 2.9.0 Docker cluster for sentiment analysis on movie reviews

## More info regarding the image will be provided later

## Run fully distributed cluster using the Makefile

* Single command to build images, start cluster, run analysis and get back results before shutting down the cluster by providing the number of workers needed (default is 1):

		make all worker=(#OFWORKERS)

	example: 
		make all worker=3

* Build images needed for master and workers

		make build worker=(#OFWORKERS)
		
* Launch hadoop cluster by using docker-compose with interactive shell

		make shell

* Launch hadoop cluster at back end

		make start

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

* clone the repository (WILL finalize this)
* cd to the directory hadoop-python-docker-sentiment
* To start pseudo-distributed cluster, run analysis and get back results before shutting down the cluster

		./pseudo-run.sh

* To start fully distributed cluster with number of workers using docker-compose, run analysis and get back results before shutting down the cluster 

		./compose-run.sh (#OFWORKERS)

	example:
		./compose-run.sh 3

* To remove the Results folders

		./clean.sh


## Run cluster on Echo using docker stack deploy (with swarm mode)

Note: This part is incomplete, still under development

The cluster can be deployed on FutureSystem Echo under the docker swarm mode. There is no point to run pseudo-distributed cluster here, the following is for fully distributed cluster:

* cd to the directory hadoop-python-docker-sentiment
* To start fully distributed cluster with number of workers using docker stack deploy, run analysis: 

		./swarm-all.sh (#OFWORKERS)

	example:
		./swarm-all.sh 3

* At the end of the previous command, there will be a http address provided such as:

		Please look for results at:
		http://149.165.150.7X:50070
		Please track jobs and resources at : 
		http://149.165.150.7X:8088/cluster

	The X here represents the physical node id that the master is running which will be provided by previous command. One could use the second address to check if job is done and then look at or download the result from the first address. 

* To remove the deployed stack after running

		./swarm-down.sh


## Benchmarking running time

Use the two following shell scripts to run customized number of iterations in order to compute average running time. This can be applied to both echo and local environment. 

* Fully distributed cluster with (#OFWORKERS) of workers and (#ITER) iterations

		./benchmark-full.sh (#ITER) (#OFWORKERS)
Result of each iteration will be written to each line of a text file at

		 ./benchmark-full/(#OFWORKERS)_worker.txt

* Pseudo-distributed cluster with (#ITER) iterations

		./benchmark-pseudo.sh (#ITER) 
Result of each iteration will be written to each line of a text file at 

		./benchmark-pseudo/pseudo.txt
