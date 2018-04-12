#! /bin/bash

# Enable ssh
echo -e "raspberry" | sudo systemctl enable ssh
echo -e "raspberry" | sudo systemctl start ssh

# Change password

echo -e "raspberry\nsnowcluster\nsnowcluster" | passwd
