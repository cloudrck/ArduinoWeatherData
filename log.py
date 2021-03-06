import serial
import calendar
import time
from datetime import datetime

com_port = '/dev/ttyACM0'
baud_rate = 9600
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
        #serial_port = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600, writeTimeout = None)
        serial_port = serial.Serial(com_port, baud_rate)
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
humidity = msg[0]
temperature = msg[1]

print(msg)

print('Humidity: ', humidity[-5:]) # Print last 5 chars, xx.xx
print('Fahrenheit: ', temperature[-5:]) # Print last 5 chars, xx.xx
print('Unix Timestamp:', timestamp)
