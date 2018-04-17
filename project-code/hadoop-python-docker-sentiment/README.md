# Apache Hadoop 2.9.0 Docker cluster for sentiment analysis on movie reviews

## More info regarding the image will be provided later

## Makefile can be used to start and shut the hadoop cluster, run analysis etc.

* single command to build images, start cluster, run analysis and get back results before shutting down the cluster:

		make all

* build images needed for master and workers

		make build
		
* launch hadoop cluster by using docker-compose with interactive shell

		make shell

* launch hadoop cluster at back end

		make start

* run the analysis after cluster is lunched

		make run

* get the analysis result

		make get

* shut down the cluster

		make down

* The information about number of workers are in docker-compose.yml

* One can check the ResourceManger at [http://localhost:8088](http://localhost:8088)



