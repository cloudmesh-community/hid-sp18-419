from sys import argv

def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

if __name__ == "__main__":
    if len(argv)>1:
        foo = getMAC(interface=argv[1])
    else:
        foo = getMAC()
    print(foo)
