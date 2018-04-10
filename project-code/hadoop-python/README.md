# Apache Hadoop 2.9.0 Docker image for sentiment analysis on movie reviews

# Build the image

If you'd like to try directly from the Dockerfile you can build the image as:

		docker build  -t minchen57/hadoop-docker-python-sentiment .


# Pull the image

		docker pull minchen57/hadoop-docker-python-sentiment


# Start a container with interactive shell

In order to use the Docker image you have just build or pulled use:

		docker run -it minchen57/minchen57/hadoop-docker-python-sentiment /etc/bootstrap.sh -bash

# Run the Map-reduce tasks to do sentiment analysis

		cd /cloudmesh/python
		./runPythonMapReduce.sh 



