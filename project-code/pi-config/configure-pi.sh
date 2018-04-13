#!/usr/bin/expect -f
set timeout -1

scp dhcp-4.3.6-P1.tar.gz pi@raspberrypi.local:/home/pi
expect "*?assword:*"
send -- "raspberry\r"
sleep 0.5
interact

spawn scp setup-pi.sh pi@raspberrypi.local:/home/pi
expect "*?assword:*"
send -- "raspberry\r"
sleep 0.2
interact

spawn ssh -t pi@raspberrypi.local:/home/pi "bash setup-pi.sh"
expect "*?assword:*"
send -- "raspberry\r"
sleep 0.2
interact
