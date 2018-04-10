# Modifying the Pi Image Before Burning to SD Card

hid-sp18-419

% status: 0

Our goal is to disable this behavior and perform the following configuraton 
automatically:
- Change the name of the machine
- [Enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
- Change the password
- Set up one of the Pis as a DHCP server

The image we are modifying can be downloaded from [Raspberry Pi](https://downloads.raspberrypi.org/raspbian_lite_latest).

Instructions are based on 
[this](http://blog.videgro.net/2015/11/modify-disk-image-raspbian/). 
Developed on Ubuntu running on VirtualBox on a Mac. It will be easier,
but less automated, to modify the image using the VM and burn the image 
with the MacOS. To burn the SD card from the VM, we will need to set up the 
VM to use the SD card device on the Mac. Instruction on how to do this are 
[here](https://superuser.com/questions/373463/how-to-access-an-sd-card-from-a-virtual-machine).

Some information on how to burn an SD image without using Etcher can be found 
[here](https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/).

One option is to copy a script to the pis, either by modifying the image 
before burning the SD card, or adding the script after boot. The latter 
can be done with scp or through a PXE boot. 

\TODO{Consider separating the startup script info into its own tutorial}

If a script is added to the image before burning, it should run on startup. 
Some strategies for doing this are described 
[here](https://askubuntu.com/questions/814/how-to-run-scripts-on-start-up). 
[Upstart](http://upstart.ubuntu.com/cookbook/#task-job) may be an option 
for running the script, but it may not be included in Raspbian. A sample 
startup script for Debian can be found 
[here](https://gist.github.com/naholyr/4275302). Information on how to run a
script at startup on the Raspberry Pi specifically can be found 
[here](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up).

To run automatically on startup, the script will need to be in one of the 
`/etc/*.d/` folders. A description of the difference between init.d and 
profile.d can be found [here](https://unix.stackexchange.com/questions/284748/custom-scripts-under-etc-profile-d-and-etc-init-d-rhel6-and-rhel7). 

A description of the first-boot activities on Raspbian Wheezy can be found 
[here](https://elinux.org/RPi_raspi-config#First-boot_activity). The process has 
changed sometime between the release of Wheezy and Stretch.  

