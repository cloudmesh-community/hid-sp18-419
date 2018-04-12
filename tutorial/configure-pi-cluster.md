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
* [Assemble a Pi Cluster](assemble-pi-cluster.md)
* [Burn SD cards with names changed and ssh enabled](modify-pi-image.md)
* Install `expect` on computer running `configure-pi.sh`. On a Mac, this is done with 
`brew install expect`. On Unix, use `apt-get install expect` or `yum install expect`.
More information on `expect` can be found [here](https://likegeeks.com/expect-command/).

