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

# Hold our function as an object
#
#['V0.80', 'C29.60', 'Fa85.28']
#
msg = serial_com()
# Assign 
voltage = msg[0]
cel = msg[1]
fa = msg[2]
print(msg)

print('Voltage: ', voltage[-4:]) # Print last 4 chars, x.xx
print('Celsius: ', cel[-5:]) # Print last 5 chars, xx.xx
print('fahrenheit: ', fa[-5:]) # Print last 5 chars, xx.xx
print('Unix Timestamp:', timestamp)
