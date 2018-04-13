#!/usr/bin/python
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
    subprocess.call(['touch', mountpoint + '/foo'])
    subprocess.call(['sudo', 'umount', mountpoint])

    # Mount the second sector and change the name
    hostname = 'foo'
    subprocess.call(['sudo', 'mount', img_name, '-o', 'offset=' + str(offset2), mountpoint])
    with open(mountpoint + '/etc/hostname', 'w+') as f:
        f.write(hostname)
    subprocess.call(['sudo', 'umount', mountpoint])
