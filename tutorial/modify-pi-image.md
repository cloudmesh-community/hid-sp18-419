# Modifying the Pi Image Before Burning to SD Card

hid-sp18-419

% status: 75

The goal is to change the hostname on the Stretch Lite images before we burn the SD cards so 
that we can use `arp -a` to populate a database matching hostnames to MAC addresses. We need 
to modify both sectors. In the first sector, we want to add an empty file called ssh so that 
we can ssh into the pi. In the second sector we change the hostname in `/etc/hostname` from 
"raspberrypi" to a dynamically generated unique name. 

NOTE: This has only been tested on an Ubuntu VM. Both the .img file and the mountpoint 
need to be on Ubuntu VM drives. The mount will fail on a Mac shared drive. 

First create a directory and download the latest build of Rasbian Lite:
```
mkdir os-images
# From raspberrypi.org
wget -O os-images/pi-img.zip https://downloads.raspberrypi.org/raspbian_lite_latest
# Raspbian for Robots from Dexter
wget -O os-images/pi-img.zip https://sourceforge.net/projects/dexterindustriesraspbianflavor/files/latest/download
```
Next unzip the file.
`unzip -d os-images/master os-images/pi-img.zip`

Copy [this script](https://github.com/cloudmesh-community/hid-sp18-419/blob/master/project-code/pi-config/make-pi-images.py) 
into the os-images directory:
```#!/usr/bin/python
import os
import sys
import subprocess
from shutil import copyfile

def get_sectors(inp):
    foo = inp.split('; ')
    startsectors = []

    for line in foo:
        if line.startswith('partition'):
            bar = line.split(', ')

            for t in bar:
                if t.startswith('startsector'):
                    startsectors.append(int(t.split(' ')[1]))

    return startsectors

if __name__ == '__main__':
    outdir = sys.argv[0] + 'output'
    hostname = 'foo'
    img_name = outdir + '/' + hostname + '.img'

    os.mkdir(outdir)
    
    copyfile(sys.argv[1], img_name)
    
    file_info = subprocess.check_output(['file', img_name])
    sectors = get_sectors(file_info)
    offset1 = int(sectors[0]) * 512
    offset2 = int(sectors[1]) * 512

    mountpoint = 'mountpoint'
    os.mkdir(mountpoint)

    # Mount the first sector and add ssh file
    subprocess.call(['sudo', 'mount', img_name, '-o', 'offset=' + str(offset1), mountpoint])
    subprocess.call(['touch', mountpoint + '/ssh'])
    subprocess.call(['sudo', 'umount', mountpoint])

    # Mount the second sector and change the name
    hostname = 'foo'
    subprocess.call(['sudo', 'mount', img_name, '-o', 'offset=' + str(offset2), mountpoint])
    with open(mountpoint + '/etc/hostname', 'w+') as f:
        f.write(hostname)
    subprocess.call(['sudo', 'umount', mountpoint])
```
 
Change into the `os-images` directory and run the script to create the custom images:

```
cd os-images
sudo python make-pi-images.py 2018-03-13-raspbian-stretch-lite.img
```
NOTE: the most current build of Raspbian Lite at the time of writing is in the command below.
You will need to replace it with the name of the current file that came out of the zip archive.

The customized image will be in a subdirectory called `make-pi-images.pyoutput`. If you run it multiple 
times, you will need to remove the `mountpoint` directory and move the `make-pi-images.pyoutput`.

## Gregor: pi-cluster-config.yaml

    data:
       images:
           dexter: https://sourceforge.net/projects/dexterindustriesraspbianflavor/files/latest/download
           rasbian: https://downloads.raspberrypi.org/raspbian_lite_latest
       hostname: red
           start: 0001
           end:   0005
       ssh: enable
       sshkey: ~/.ssh/id_rsa.pub
       passwd:  readline 
       
## Gregor: Manual page cmd5 may be easier than click.

    modify-sdcard -fecth [rasbian|dexter|https://downloads.raspberrypi.org/raspbian_lite_latest]  - fetched the image
    modify-sdcard -burn IMAGE   - puts the given image on the sd card
    modify-sdcard -ssh [enable|disable] enables or disables ssh 
    modify-sdcard -sshkey [~/.ssh/id_rsa.pub]  puts the default key for login
    modify-sdcard -name NAME puts the given name on the image
    

/TODO Loop to create multiple images, handle exception of existing mountpoint and output directory

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

