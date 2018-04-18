DESTDIR=Results
worker=1

dest:
	mkdir -p $(DESTDIR)

all: build start run get down

scale:
	@echo "making docker-compose.yml with 1 master and $(worker) worker(s)"
	./scale.sh $(worker)

build:scale 
	@echo "building images for master and worker..."
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
	@echo "build the cluster with 1 master and $(worker) worker(s)"
	docker-compose build
	@echo "DONE"


start:
	@echo "starting the containers..."
	docker-compose up -d
	echo "http://localhost:9870 for HDFS"
	echo "http://localhost:8088 for YARN"

shell: start
	echo "Now interactive shell for master..."
	docker exec -it master bash

run:
	echo "running the sentiment analysis on movie reviews..."
	docker exec master /etc/runall.sh

get: clean dest
	@echo "getting the results..."
	docker cp master:/cloudmesh/python/output_pos_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/output_neg_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/log.txt ./$(DESTDIR)
	mv docker-compose.yml ./$(DESTDIR)
	

down:
	@echo "shutting down the cluster..."
	docker-compose down


clean:
	rm -rf $(DESTDIR)

		
