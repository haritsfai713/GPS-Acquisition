# Library
import serial #library for serial communication
import pynmea2 #library for parsing GPS NMEA format
import socketio
import json
#import time #library for time
#import datetime #library for date & time

#initialize variable
global lat
global lon

sio = socketio.Client()
sio.connect("http://localhost:3000") #adjust the localhost with address of Client PC

# Serial communication
try:
    ser = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=1)
    print("Connected to GPS SE100 NMEA")
except:
    print("Disconnected to GPS SE100 NMEA")

#ser.reset_input_buffer()
    
# Algorithm of GPS SE100 NMEA
while True:
    try:
        #if ser.in_waiting > 0:
            # Decode the data from GPS SE100 NMEA serial communication
            line = ser.readline().decode('utf-8', errors='replace')
            line = line.strip()
            #print(line)
        
            # Select the $GNGGA only
            if '$GNGGA' in line:
                #print(line)
                
                # Parse the data by using pynmea library
                msg = pynmea2.parse(line)
                #print(msg)
                #print(repr(msg))
        
                # Timer
                #timer = datetime.datetime.now()
            
                # Variable
                lat = msg.latitude
                lon = msg.longitude
                sats = msg.num_sats
                hdop = msg.horizontal_dil

                gps_data = {"id": 1,
                "data": {
                    "latitude": lat,
                    "longitude": lon,
                    "status": "GPS Not Ready",
                    "vehicleName": "Car A"
                }
                }
                gps2json = json.dumps(gps_data)
                print(gps2json)
                sio.emit("gps",gps2json)
        
                # Print the data GPS NMEA SE100 Radiolink
                #print("Time                             :", timer.strftime("%Y-%m-%d %H:%M:%S"))
                #print("================================")
                #print("Latitude                         :", lat)
                #print("Longitude                        :", lon)
                #print("Number satellite                 :", sats)
                #print("Horizontal Dilution of Precision :", hdop)
                #print("================================")
                print("gps")
            
                # Database Connection
                # db = pymysql.connect(host='192.168.18.19',
                #                      user='itbdelabo',
                #                      password='delabo0220',
                #                      db='monitoring',
                #                      charset='utf8',
                #                      cursorclass=pymysql.cursors.DictCursor)
                # cur = db.cursor()
            
                # add_c0 = "INSERT INTO `gps_msd700`(timestamp, latitude, longitude, satellite, hdop) VALUES (%s,%s,%s,%s,%s)"
                # cur.execute(add_c0,((timer.strftime("%Y-%m-%d %H:%M:%S"),
                #                      lat,
                #                      lon,
                #                      sats,
                #                      hdop)))
                # db.commit()
        
                # # Delay time
                # time.sleep(2)
    except:
        #Disconnected
        #print("GPS NMEA SE100 DATA is not sent")
        #print("================================")
        #print("")
        #time.sleep(5)
        pass

# Check the GPS sentence formats
# import serial
# with serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1) as ser:
#     # read 10 lines from the serial output
#     for i in range(100);
#         line = ser.readline().decode('ascii', errors='replace')
#         print(line.strip())

# Parse the data by using pynmea library
# msg = pynmea2.parse(line)
# print(msg)
# for msg in msg.split('\n'):
# if msg.startswith('$GNGGA') :
# print(repr(msg))
