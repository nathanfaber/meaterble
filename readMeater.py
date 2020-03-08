#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Find the meater address with hcitool lescan (label MEATER).
# run readMeater.py <address>
# python ./readMeater.py D0:D9:4F:83:E8:EB
# Connecting...
# Connected
# 50,2,21,0,19,0,9,0
# tip: 50 2 (94.980000F) tail: 21 0 (160.840000F)
# 50,2,22,0,19,0,9,0
# tip: 50 2 (94.980000F) tail: 22 0 (161.880000F)
# 50,2,22,0,19,0,9,0
# tip: 50 2 (94.980000F) tail: 22 0 (161.880000F)
# 50,2,23,0,19,0,9,0
# tip: 50 2 (94.980000F) tail: 23 0 (162.920000F)
# 50,2,23,0,19,0,9,0
# tip: 50 2 (94.980000F) tail: 23 0 (162.920000F)

import time
from bluepy import btle
import sys
import time
import pickle
import binascii

from meaterTemperature import Temperature
 
print "Connecting..."
addr = sys.argv[1]
dev = btle.Peripheral(addr)
print "Connected"

def enumerateDev(dev):
    for (ks, svc) in enumerate(dev.services):
        print str(svc)
        for (k,c) in enumerate(svc.getCharacteristics()):
            r = c.read()
            print ks
            print k
            print `r`
            print binascii.b2a_hex(c.read())
            print


service=dev.services[2]
char=service.getCharacteristics()[1]
fp=open(addr + ".pickle", "ab")
while True:
    r1 = bytearray(char.read())
    print ("".join("0x%02x, " % i for i in r1))

    temp = Temperature(r1)
    print "    tip: %s %d %fF (%fC)" % (hex(temp.getTip()), temp.getTip(), temp.getTipF(), temp.getTipC())
    print "ambient: %s %d %fF (%fC)" % (hex(temp.getAmbient()), temp.getAmbient(), temp.getAmbientF(), temp.getAmbientC())
    print ""

    pickle.dump((time.time(), r1), fp)
    fp.flush()
    time.sleep(1)
