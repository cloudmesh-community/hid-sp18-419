class Disk(object):
    def __init__(self, 
                 platform, 
                 disk_size, 
                 disk_used, 
                 disk_free,
                 disk_percent):

        self.platform = platform
        self.disk_size = disk_size
        self.disk_used = disk_used
        self.disk_free = disk_free
        self.disk_percent = disk_percent
