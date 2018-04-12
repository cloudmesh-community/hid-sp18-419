# Automated Headless Configuration of a Pi Cluster

hid-sp18-419

% status: 0

Our goal is perform the following configuraton automatically:

* [Enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/) 
permanently (initial ssh access will be enabled when we burn the SD cards)
* Change the password
* Set up one of the Pis as a DHCP server

These actions are all done with two scripts. The first script, `configure-pi.sh`,
runs on the computer used to set up the Pis. The second, `setup-pi.sh`, enables ssh, 
changes the password for the pi user, and configures the master node as a DHCP server.
Determination of whether the node is the master or a worker is done with the `-m` flag.

## Prerequisites
* Assemble a Pi Cluster
* Burn SD cards with names changed and ssh enabled


