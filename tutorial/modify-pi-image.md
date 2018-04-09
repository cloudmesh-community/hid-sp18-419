# Modifying the Pi Image Before Burning to SD Card

hid-sp18-419

% status: 0

The first boot behavior of the Pi is described 
[here](https://elinux.org/RPi_raspi-config#First-boot_activity).
Our goal is to disable this behavior and perform the following configuraton 
automatically:
- Change the name of the machine
- [Enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
- Change the password
- Set up one of the Pis as a DHCP server

Instructions are based on 
[this](http://blog.videgro.net/2015/11/modify-disk-image-raspbian/). 
Developed on Ubuntu running on VirtualBox on a Mac.

One option is to copy a script to the pis, either by modifying the image 
before burning the SD card, or adding the script after boot. The latter 
can be done with scp or through a PXE boot. 

If a script is added to the image before burning, it should run on startup. 
Some strategies for doing this are described 
[here](xhttps://askubuntu.com/questions/814/how-to-run-scripts-on-start-up). 
[Upstart](http://upstart.ubuntu.com/cookbook/#task-job) may be an option 
for running the script, but it may not be included in Raspbian.

