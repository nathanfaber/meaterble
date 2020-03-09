#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Find the meater address with hcitool lescan (label MEATER).
# run readMeater.py <address>
# python ./readMeater.py D0:D9:4F:83:E8:EB

import time
from bluepy import btle
import sys
import time
import pickle
import binascii

from meater import MeaterProbe
 
print "Connecting..."
devs = [MeaterProbe(addr) for addr in sys.argv[1:]]
print "Connected"

while True:
    for dev in devs:
       dev.update()
       print dev
    time.sleep(1)
