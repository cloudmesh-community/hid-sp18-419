#!/bin/bash

# If connected to the internet
sudo apt-get update
sudo apt-get install isc-dhcp-server

# If not connected to the internet
tar -zxf /home/pi/dhcp-4.3.6-P1.tar.gz
cd dhcp-4.3.6-P1
./configure
make
sudo make install

cat <<EOT >> /etc/dhcp/dchpd.conf
subnet 192.168.2.0 netmask 255.255.255.0 {
    range 192.168.2.100 192.168.2.200;
    option broadcast-address 192.168.2.255;
    option routers 192.168.2.1;
    max-lease-time 7200;
    option domain-name "red00";
    option domain-name-servers 8.8.8.8;
}
EOT

sed -i -e 's/INTERFACES=\"\"/INTERFACES=\"eth0\"/g' /etc/default/isc-dhcp-server

sed -i -e 's/iface eth0 inet dhcp/\# iface eth0 inet dhcp/g' /etc/network/interfaces

cat <<EOT >> /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.2.1
    netmask 255.255.255.0
}
EOT

sudo service isc-dhcp-server stop
sudo service isc-dhcp-server start

