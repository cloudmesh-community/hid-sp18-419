Instructions: https://medium.com/@viveks3th/how-to-bootstrap-a-headless-raspberry-pi-with-a-mac-6eba3be20b26

brew install nmap
Add image to sd card using Etcher
Add ssh file to SD card
 - cd /Volumes/boot
 - touch ssh
Connect mac to switch
Turn on internet sharing - share with switch
- Used iPhone internet because IU wifi is protected by 801.x (make sure this is correct)
ifconfig | grep "inet " to get mac ip address
Use nmap to find ip address of pi: e.g. if ifconfig returned 192.168.2.255, you would use the command: nmap -n -sP 192.168.2.255/24
Enable SSH permanently (https://www.raspberrypi.org/documentation/remote-access/ssh/):
 - sudo raspi-config
 - Interfacing Options
 - SSH
 - Yes
 - OK
 
 from: https://raspberrypi.stackexchange.com/questions/19579/ssh-into-pi-from-mac-over-direct-ethernet-connection
 https://bneijt.nl/blog/post/enable-ipv6-on-your-raspberry-pi/
 add ipv6 to the end of /etc/modules
 reboot
 ssh pi@red01.local
 Now you will be able to ssh into the pi without internet sharing


