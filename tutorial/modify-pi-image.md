# Modifying the Pi Image Before Burning to SD Card

hid-sp18-419

% status: 0

The first boot behavior of the Pi is described [here](https://elinux.org/RPi_raspi-config#First-boot_activity).
Our goal is to disable this behavior and perform the following configuraton automatically:
- Change the name of the machine
- Enable ssh
- Change the password
- Set up one of the Pis as a DHCP server

Instructions are based on [this](http://blog.videgro.net/2015/11/modify-disk-image-raspbian/). 
Developed on Ubuntu running on VirtualBox on a Mac.

[Upstart](http://upstart.ubuntu.com/cookbook/#task-job) may be an option for running the script, but it may not be included in Raspbian.

