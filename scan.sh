#!/bin/bash
hciconfig hci0 down
hciconfig hci0 up
timeout 5 stdbuf -o 0 hcitool lescan | egrep --line-buffered MEATER | tee /dev/stderr
