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
```
## Preliminary Requirements
The service requires that you have:
* A Google Cloud Platform account
* The Gcloud API installed
* Default variables: project and compute zone configured.
* Enable [Cloud Resource Manager API](https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview)

[This tutorial](https://github.com/cloudmesh/book/blob/master/tutorial/google-compute-engine.md)
walks through the whole process.
