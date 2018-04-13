#
# Naturally you need to adapt this to make work for your project
#

all:
	@echo "create a useful makefile that makes it easy to run your code"
	@echo make sure your data is downloaded from the intenet"

master-image:
	mkdir os-images
	wget -O os-images/pi-img.zip https://downloads.raspberrypi.org/raspbian_lite_latest
	mkdir os-images/master
	unzip -d os-images/master os-images/pi-img.zip
	SECTORSTARTS=$(file os-images/master/*.img | python parse-find.py)

configure-pi:
	curl -s -o dhcp-4.3.6-P1.tar.gz https://www.isc.org/downloads/file/dhcp-4-3-6-p1/?version=tar-gz


clean: 
	rm -R os-images

data:
	@echo "wget or curl your data from the internet"

generate:
	@echo "generat your code such as swagger services"

install: install-swagger install-mongo
	@echo "install your code so it can be used on the system it is supposed to run"
	@echo "you could have multiple installs so we giva na exampel"

install-swagger:
	@echo "install your swagger services"

install-mongo:
	@echo "install your mongo services - this is just an example, you may not use mongo"

start: start-swagger start-mongo
  @echo "start your code so it can be used on the system it is supposed to run"
	@echo "you could have multiple starts so we giva na exampel"

start-swagger:
	@echo "start your swagger services"

stop-mongo:
	@echo "stop your mongo services - this is just an example, you may not use mongo"

stop: stop-swagger stop-mongo
  @echo "stop your code so it can be used on the system it is supposed to run"
	@echo "you could have multiple stops so we giva na exampel"

stop-swagger:
	@echo "stop your swagger services"

stop-mongo:
	@echo "stop your mongo services - this is just an example, you may not use mongo"

test:
	@echo "test your service"


