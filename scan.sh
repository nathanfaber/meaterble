#!/bin/bash
#my rpi hci0 interfaces seems to get out of wack. bounce it.
sudo hciconfig hci0 down
sudo hciconfig hci0 up
sudo timeout 5 stdbuf -o 0 hcitool lescan | egrep --line-buffered MEATER | tee /dev/stderr
