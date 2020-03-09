#!/bin/bash
./scan.sh | awk '{print $1}' | xargs -r -P8 -n1 python ./readMeater.py 
