# REST Service with Swagger
The makefile was adapted from [Arnav](https://github.com/cloudmesh-community/hid-sp18-503). The `stop` 
strategy was adapted from [Min Chen](https://github.com/cloudmesh-community/hid-sp18-405).

These work:
```
make service
make start
make clean
make stop
make test
make container
make container-start
make container-stop
```
## Preliminary Requirements
The service requires that you have:
* A Google Cloud Platform account
* The Gcloud API installed

A service account has been provided for testing. 

[This tutorial](https://github.com/cloudmesh/book/blob/master/tutorial/google-compute-engine.md)
walks through the whole process.
