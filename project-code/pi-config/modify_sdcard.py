import argparse
import sys
from Crypto.PublicKey import RSA
from shutil import copyfile
import os

class PiImage:
    def __init__(self, hostname, path):
        self.hostname = hostname
        self.outputfile = path + hostname + '.img'
        self.home = '/home/pi'
        self.mountpoints = []
        self.pubkey = ''

        
    def create_mountpoints(self, sectors):
        for i, sector in enumerate(sectors):
            mp = self.hostname + '_{}'.format(i)
            os.mkdir(mp)
            subprocess.call(['sudo', 'mount', self.outputfile, '-o', 'offset=' + str(sector), mp])
            self.mountpoints.append(mp)

            
    def create_key(self):
        key = RSA.generate(2048)
        p = self.mountpoints[1] + self.home + '/.ssh'
        os.mkdir(p)
        with open(p + 'id_rsa', 'w') as f:
            os.chmod(p + 'id_rsa', 0600)
            f.write(key.exportKey('PEM'))
        self.pubkey = key.publickey()
        with open(p + 'id_rsa.pub', 'w') as f:
            f.write(pubkey.exportKey('OpenSSH'))
        

    def remove_mountpoints(self):
        for mp in self.mountpoints:
            subprocess.call(['sudo', 'unmount',  mp])
            os.rmdir(mp)
        self.mountpoints = []

        
    def change_hostname(self):
        with open(self.mountpoints[1], 'w') as f:
            f.write(self.hostname)
            f.close()

            
    def enable_ssh(self):
        open(self.mountpoints[0] + '/ssh', 'a').close()

        
    def add_auth_key(self, key):
        with open(self.mountpoints[1] + self.home + '/.ssh/authorized_keys', 'a') as f:
            f.write(key)
            f.close()

    def put_auth_key(self, pi):
        with open(pi.mountpoints[1] + pi.home + '/.ssh/authorized_keys', 'a') as f:
            f.write(self.pubkey)
            f.close()

        
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
        

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def create_name(number, name):
    return name + '{:03}'.format(number)


def make_outdir(basename, suffix):
    outdir = basename + suffix
    os.mkdir(outdir)
    return outdir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssh",
                        type=str2bool,
                        nargs='?',
                        const=True,
                        help="Enable ssh on images")
    parser.add_argument("--sshkey",
                        help="Add public key to boot images")
    parser.add_argument("--basename",
                        type=str,
                        default="snowcluster",
                        help="Base hostname for Pis")
    parser.add_argument("--start",
                        type=int,
                        default=0,
                        help="Starting number for names")
    parser.add_argument("--num",
                        type=int,
                        default=1,
                        help="Number of images to create")
    parser.add_argument("image",
                        type=str,
                        help="Image file to modify")

    args = parser.parse_args()
    sectors = get_sectors(args.image)
    outdir = make_outdir(args.basename, '_images')

    images = []
    for i in range(args.num):
        pi = PiImage(create_name(basename, i + args.start), outdir)
        pi.create_mountpoints(sectors)
        pi.change_hostname()
            
    if args.ssh:
        for pi in images:
            pi.enable_ssh()
            pi.create_key()
            for other_pi in images:
                if pi.hostname != other_pi.hostname:
                    pi.put_auth_key(other_pi)
    if args.sshkey:
        for pi in images:
            with open(args.sshkey, 'r') as f:
                pi.add_auth_key(f.read())
                f.close()

    for pi in images:
        pi.remove_mountpoints()
    
    
if __name__ == '__main__':
    main()
