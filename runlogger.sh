#!/bin/sh

cd /home/pi/twc-logger/data
curl -s http://192.168.86.46/api/1/vitals | python3 /home/pi/twc-logger/twclogger.py
rclone copy /home/pi/twc-logger googledrive:twc-logger

