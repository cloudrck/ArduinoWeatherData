import serial
import calendar
from datetime import datetime
  
ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600, writeTimeout = None)

  
while True:
    d = datetime.utcnow()
    timestamp=calendar.timegm(d.utctimetuple())
    #message = ser.readline().strip(b'\x00').decode('ascii')
    message = ser.readline()
    print(message)
    #print(timestamp)
    #time.sleep(0.5)
    
