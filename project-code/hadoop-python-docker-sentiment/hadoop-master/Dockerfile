# Hadoop 2.9.0 cluster on Docker with Python Map-Reduce through Hadoop-streaming
#
# Application: sentiment analysis on movie review (Polarity 2.0 data)
#
# This Dockerfile creates image for master node
# 
# docker build  -t minchen57/hadoop-python-docker-sentiment-master .
#
# Modified from sequenceiq/hadoop-docker <https://github.com/sequenceiq/hadoop-docker>
# Modified from Lewuathe/docker-hadoop-cluster <https://github.com/Lewuathe/docker-hadoop-cluster>


FROM minchen57/hadoop-docker-python-sentiment-compose-base:latest
MAINTAINER Min Chen

RUN service sshd start
ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

ENV BOOTSTRAP /etc/bootstrap.sh

# Copy the python scripts and download data
RUN mkdir -p /cloudmesh/python/data
COPY python/*py /cloudmesh/python/
COPY python/*sh /cloudmesh/python/
RUN chmod +x /cloudmesh/python/*.py /cloudmesh/python/*.sh
RUN curl -s http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz | tar -xz -C /cloudmesh/python/data
RUN mv /cloudmesh/python/split_data.sh /cloudmesh/python/data/split_data.sh


COPY python/runall.sh /etc/runall.sh
COPY python/startup.sh /etc/startup.sh
RUN chmod +x /etc/runall.sh
RUN chmod +x /etc/startup.sh

CMD ["/etc/bootstrap.sh", "-d"]
