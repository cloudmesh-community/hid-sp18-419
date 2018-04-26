# Raspberry Pi Configuration Scripts

To download the latest version of Raspbian Stretch Lite: 
```
bash download_image.sh
```

To create custom images for a Pi cluster:
```
sudo pip install -r requirements.txt
sudo python modify_sdcard.py <flags> <base_image>
```
It needs to be run on Linux and has only been tested on Ubuntu 16.04. It will 
not work on a Mac. The machine running the script will need 1.9GB times the number of images 
created of free disk space. The base image is used to create the number of images specified
with the `--num` flag. A list of available flags is available with:
```
python modify_sdcard.py -h
usage: modify_sdcard.py [-h] [--ssh [SSH]] [--sshkey SSHKEY]
                        [--basename BASENAME] [--start START] [--num NUM]
                        image

positional arguments:
  image                Image file to modify

optional arguments:
  -h, --help           show this help message and exit
  --ssh [SSH]          Enable ssh on images
  --sshkey SSHKEY      Add public key to boot images
  --basename BASENAME  Base hostname for Pis
  --start START        Starting number for names
  --num NUM            Number of images to create
```
For example, to create 5 images from the latest Raspbian Stretch Lite image, 
labeled `lavender003-lavender007` enabling ssh and copying the ssh key from 
a setup computer to all the pis, the command would be:
```
sudo -H python modify_sdcard.py --num 5\
                                --basename=lavender\
                                --ssh=y\
                                --sshkey=<public key file>\ 
                                --start=3\
                                2018-04-18-raspbian-stretch-lite.img
```
The `--ssh` flag defaults to true, `--basename` defaults to `snowcluster`, and 
`--num` defaults to 1.

## Known issues:
Because the script needs to be run as root, `~/.ssh` and its contents: `id_rsa`, 
`id_rsa.pub`, and `authorized_keys` are owned by root. 

## Next Steps
* Fix permissions problem
* Create keys for `known_hosts` and populate to all images
* Set fixed IP address on all Pis
* Incorporate `download_image.sh` functionality into script, with option to select 
a different base OS (e.g. from Dexter Labs)
* Add option to burn images from the script. 
* Write post configuration setup scripts:
  * Make the head node a DHCP server
  * Create a DB of IP addresses, Mac Addresses, and hostnames
  * Permanenty enables ssh
  * Change password
