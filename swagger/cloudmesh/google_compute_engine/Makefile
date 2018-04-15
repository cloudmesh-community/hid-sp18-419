# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile
# assumes Makefile is in Directory named for service specified

swagger_codegen:=java -jar swagger-codegen-cli-2.3.1.jar

SWAGGER:=${swagger_codegen}

SPEC:=${shell ls *.yml}
SERVICE:=${SPEC:%.yml=%}

all: service requirements run
	@echo "DONE"

service:
	pip install -r requirements.txt
	sh setup.sh

	cd server/${SERVICE}/flaskConnexion; pip install -r requirements.txt
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGER) generate \
		-i ${SPEC} \
		-l python-flask \
		-o server/${SERVICE}/flaskConnexion \
		-D supportPython2=true
	cp default_controller.py server/${SERVICE}/flaskConnexion/swagger_server/controllers/


start:
	cd server/${SERVICE}/flaskConnexion/ &&\
	python -m swagger_server

stop:
	ps -aux | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9


test:
	curl -X GET --header 'Accept: application/json' 'http://localhost:8080/cloudmesh/google_compute_engine/vms'

clean:
	rm -rf server/
	rm swagger-codegen-cli-2.3.1.jar
