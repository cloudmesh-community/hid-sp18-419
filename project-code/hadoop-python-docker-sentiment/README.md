# Apache Hadoop 2.9.0 Docker cluster for sentiment analysis on movie reviews

## One can use the Makefile to start and shut the hadoop cluster

* build images needed for master and workers

		make all
		
* launch hadoop cluster by using docker-compose with interactive shell

		make run

* shut down the cluster

		make down

* The information about number of workers are in docker-compose.yml

## Test the whole analysis

* Start the cluster with shell

		make all
		make run

* Run the script (with timer)

		time /cloudmesh/python/runPythonMapReduce.sh

* One can check the ResourceManger at [http://localhost:8088](http://localhost:8088)



