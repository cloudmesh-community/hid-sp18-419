# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile
# assumes Makefile is in Directory named for service specified

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
	cp *_controller.py server/${SERVICE}/flaskConnexion/swagger_server/controllers/  

start:
	cd server/${SERVICE}/flaskConnexion/ &&\
	python -m swagger_server

stop:
	ps | grep swagger_server | grep -v "grep" | awk '{print $$1}' | xargs kill -9

clean:
	rm -rf server/
