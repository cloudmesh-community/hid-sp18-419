# Raspbian headless setup on a Mac (a work in progress)

Most instructions are [here](https://medium.com/@viveks3th/how-to-bootstrap-a-headless-raspberry-pi-with-a-mac-6eba3be20b26).

`brew install nmap`

Add image to sd card using Etcher

Add ssh file to SD card
 - `cd /Volumes/boot`
 - `touch ssh`

Connect mac to hub

Turn on internet sharing - share with hub
- Used iPhone internet because IU wifi is protected by 801.x 
`ifconfig | grep "inet "` to get mac ip address

Use nmap to find ip address of pi: e.g. if ifconfig returned 192.168.2.255, 
you would use the command: 

`nmap -n -sP 192.168.2.255/24`

Enable SSH permanently 
([instructions](https://www.raspberrypi.org/documentation/remote-access/ssh/)):
 - `sudo raspi-config`
 - Interfacing Options>SSH>Yes>OK (There has to be a better way of doing this)
 
Add ipv6 to the end of the file "/etc/modules" on the pi so you can ssh using the name 
instead of the IP address and don't have to use network sharing anymore. (From [here](https://raspberrypi.stackexchange.com/questions/19579/ssh-into-pi-from-mac-over-direct-ethernet-connection) 
and [here](https://bneijt.nl/blog/post/enable-ipv6-on-your-raspberry-pi/))

reboot

Now you can ssh using the name of the machine. For me the command is:

`ssh pi@red01.local`

[Running a script on startup](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)

To run a scipt at startup, the script needs to be added to /etc/init.d/

Instead of using the GUI, ssh can be enabled with the following commands:

`update-rc.d ssh enable`
`invoke-rc.d ssh start`

[Changing hostname](https://raspberrypi.stackexchange.com/questions/44955/config-txt-hostname)

Change the string in /etc/hostname

Building a custom raspbian image:

https://github.com/RPi-Distro/pi-gen
https://github.com/niklasf/build-raspbian-image
https://github.com/andrius/build-raspbian-image
https://www.raspberrypi.org/blog/pibakery/

[Latest source](http://archive.raspbian.org/raspbian/dists/stretch/)

## Modifications to image
* enable ssh
* change hostname
* [modify password via script](https://stackoverflow.com/questions/27837674/changing-a-linux-password-via-script)
* get mac addresses
* set ip addresses
