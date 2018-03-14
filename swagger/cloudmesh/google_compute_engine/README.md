# REST Service with Swagger
I copied the makefile from [Arnav](https://github.com/cloudmesh-community/hid-sp18-503) and modified it.
Feel free to copy mine. You shouldn't have to modify it as much (if at all.)

[Here's a good place to learn about makefiles](https://ftp.gnu.org/old-gnu/Manuals/make-3.79.1/html_chapter/make_6.html).

These work:
```
make service
make start
make clean
```

Still need to figure out:
```
make stop
make test
```

When the server is running, you can see the output with: 
```
curl -X GET --header 'Accept: application/json' 'http://localhost:8080/cloudmesh/google_compute_engine/vms'
```
(I should probably throw that into test...)

To make anything happen at this point, you will need to do some additional setup as described below. 

## Setup instructions - Ubuntu (Work in progress)

* Project name and zone must be set in default_controller.py

## Google Compute Engine: VM Instance

[Google's documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

### Authentication
`pip install --upgrade google-api-python-client`

`pip install --upgrade google-auth-httplib2`

Sample code is [here](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/api)
