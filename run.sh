#!/bin/bash
./scan.sh | awk '{print $1}' | xargs -P8 -n1 python ./readMeater.py 
