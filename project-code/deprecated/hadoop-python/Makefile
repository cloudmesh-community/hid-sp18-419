DESTDIR=Results
HADOOP_VERSION=2.9.0

all: build run get stop
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

build:
	@echo "Build the image from docker file"
	docker build  -t minchen57/hadoop-docker-python-sentiment:$(HADOOP_VERSION) . 

run:  
	@echo "Run the container with sentiment analysis on hadoop"
	docker run -it minchen57/hadoop-docker-python-sentiment:$(HADOOP_VERSION)

get: clean dest
	@echo "Get the results"
	docker cp $$(docker ps -alq):/cloudmesh/python/output_pos_tagged ./$(DESTDIR)
	docker cp $$(docker ps -alq):/cloudmesh/python/output_neg_tagged ./$(DESTDIR)
	docker cp $$(docker ps -alq):/cloudmesh/python/log.txt ./$(DESTDIR)

stop:
	@echo "Stop the container"
	docker stop $$(docker ps -alq)

clean:
	rm -rf $(DESTDIR)

container: build
	@echo "Start the container with interactive shell"
	docker run -it minchen57/hadoop-docker-python-sentiment:$(HADOOP_VERSION) /etc/bootstrap.sh -bash 
