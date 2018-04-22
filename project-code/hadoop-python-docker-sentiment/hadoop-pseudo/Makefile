DESTDIR=Results

all: build run get stop
	@echo "DONE"
	

dest:
	mkdir -p $(DESTDIR)

build:
	@echo "Build the image from docker file"
	docker build  -t minchen57/hadoop-docker-python-sentiment-pseudo:latest . 

run:  
	@echo "Run the container with sentiment analysis on hadoop"
	docker run -it --name pseudo-hadoop minchen57/hadoop-docker-python-sentiment-pseudo:latest

get: clean dest
	@echo "Get the results"
	docker cp pseudo-hadoop:/cloudmesh/python/output_pos_tagged ./$(DESTDIR)
	docker cp pseudo-hadoop:/cloudmesh/python/output_neg_tagged ./$(DESTDIR)
	docker cp pseudo-hadoop:/cloudmesh/python/log.txt ./$(DESTDIR)

stop:
	@echo "Stop the container"
	docker stop pseudo-hadoop
	docker rm pseudo-hadoop

clean:
	rm -rf $(DESTDIR)

container: build
	@echo "Start the container with interactive shell"
	docker run -it --name pseudo-hadoop minchen57/hadoop-docker-python-sentiment-pseudo:latest /etc/bootstrap.sh -bash 

		
