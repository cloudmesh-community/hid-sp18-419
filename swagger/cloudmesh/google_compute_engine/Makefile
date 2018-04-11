# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile
# assumes Makefile is in Directory named for service specified

GCP_PROJECT:=$(shell gcloud config get-value project)
GCP_ZONE:=$(shell gcloud config get-value compute/zone)

swagger_codegen:="swagger-codegen"

SWAGGER:=${swagger_codegen}

SPEC:=${shell ls *.yml}
SERVICE:=${SPEC:%.yml=%}

all: service requirements run
	@echo "DONE"

service:
	pip install -r requirements.txt
	cd server/${SERVICE}/flaskConnexion; pip install -r requirements.txt
	$(SWAGGER) generate \
		-i ${SPEC} \
		-l python-flask \
		-o server/${SERVICE}/flaskConnexion \
		-D supportPython2=true
	cp default_controller.py server/${SERVICE}/flaskConnexion/swagger_server/controllers/
	awk -i inplace 'BEGINFILE{print "GCP_PROJECT=\"${GCP_PROJECT}\"\nGCP_ZONE=\"${GCP_ZONE}\""}{print}' server/${SERVICE}/flaskConnexion/swagger_server/controllers/default_controller.py

start:
	cd server/${SERVICE}/flaskConnexion/ &&\
	python -m swagger_server

stop:
	ps | grep swagger_server | grep -v "grep" | awk '{print $$1}' | xargs kill -9

test:
	curl -X GET --header 'Accept: application/json' 'http://localhost:8080/cloudmesh/google_compute_engine/vms'

clean:
	rm -rf server/
