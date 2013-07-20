import serial
import calendar
import time
from datetime import datetime

# Set some UTC time
d = datetime.utcnow()
timestamp=calendar.timegm(d.utctimetuple())

#lines = serial_com
#lines[-1]              

# Returns List
def serial_com():
    '''Serial communications: get a response'''

    # open serial port
    try:
        serial_port = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600, writeTimeout = None)
    except serial.SerialException as e:
        print("could not open serial port '{}': {}".format(com_port, e))

    # read response from serial port
    lines = []
    while True:
        line = serial_port.readline()
        lines.append(line.decode('utf-8').rstrip())

        # wait for new data after each line
        timeout = time.time() + 0.1
        while not serial_port.inWaiting() and timeout > time.time():
            pass
        if not serial_port.inWaiting():
            break 

    #close the serial port
    serial_port.close()   
    return lines

msg = serial_com()    
print(msg)
print('Voltage: ', msg[0])
print('Celsius: ', msg[1])
print('fahrenheit: ', msg[2])
print(timestamp)
