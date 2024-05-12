"""
#!/usr/bin/env python
#title           :gps_serial.py
#description     :Python Script Communication between GPS SE100 NMEA and Raspberry Pi
#author          :Fajar Muhammad Noor Rozaqi
#date            :2022/11/14
#version         :0.2
#usage           :Python
#notes           :
#python_version  :3.8
#==============================================================================
"""

# Library
#import serial #library for serial communication
import pynmea2 #library for parsing GPS NMEA format
import socketio
import json
import time
#import time #library for time
#import datetime #library for date & time

#initialize variable
global lat
global lon

sio = socketio.Client()
# sio.connect("http://172.22.31.125:3000")
sio.connect("http://192.168.18.160:3000")

# Serial communication
#try:
    #ser = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=1)
    #print("Connected to GPS SE100 NMEA")
#except:
    #print("Disconnected to GPS SE100 NMEA")

#ser.reset_input_buffer()
    
    
while True:

	payload = {"id": 1,
                "data": {
                    "latitude": 33.2108277,
                    "longitude": 130.0459166,
                    "status": "GPS Not Ready",
                    "vehicleName": "Car A"
                }
                }
	gps2json = json.dumps(payload)
	print(gps2json)
	sio.emit("gps",gps2json)
	time.sleep(1)


