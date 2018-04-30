DESTDIR=Results
worker=1

dest:
	mkdir -p $(DESTDIR)

all: build start run get down

build:
	@echo "building images for master and worker..."
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
	@echo "remove previous network"
	docker-compose down
	if docker network rm hadoop-sentiment; then :; else :; fi
	@echo "create the network"
	docker network create hadoop-sentiment
	@echo "DONE"


start:
	@echo "starting the containers..."
	docker-compose scale master=1 worker=$(worker)
	@echo "http://localhost:50070 for HDFS"
	@echo "http://localhost:8088 for YARN"
	@echo "if you are on Echo, use 149.165.150.76 to replace localhost"

shell: start
	@echo "Now interactive shell for master..."
	docker exec -it master bash

run:
	@echo "pause for 30 seconds"
	sleep 30
	@echo "running the sentiment analysis on movie reviews..."
	docker exec master /etc/runall.sh

get: clean dest
	@echo "getting the results..."
	docker cp master:/cloudmesh/python/output_pos_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/output_neg_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/log.txt ./$(DESTDIR)
	cp docker-compose.yml ./$(DESTDIR)
	

down:
	@echo "shutting down the cluster..."
	docker-compose down
	docker network rm hadoop-sentiment


clean:
	rm -rf $(DESTDIR)
	

		
