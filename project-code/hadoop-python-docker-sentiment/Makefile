all:
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
	docker-compose build

.PHONY: test clean

run:
	docker-compose up -d
	echo "http://localhost:9870 for HDFS"
	echo "http://localhost:8088 for YARN"
	echo "Now interactive shell for master..."
	docker exec -it master bash

down:
	docker-compose down
