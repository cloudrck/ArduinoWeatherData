#!/usr/bin/python

import os
import sys
import serial
import gtk
import pygtk
import calendar
import time
from datetime import datetime

com_port = '/dev/ttyACM0'
baud_rate = 9600

class MyScript():
    #global textarea
    
    def __init__(self):
    	global textbuffer
    	
  	textbuffer = textarea.get_buffer()
  	#msg = self.serial_com()
    	print('init')
    	
    def closeDown(self, *args):
    	gtk.main_quit(*args)
    	

    def printview(self, button):
    	#textbuffer = textarea.get_buffer()
    	msg = self.serial_com()
    	# Assign 
    	humidity = msg[0]
    	temperature = msg[1]
    	d = datetime.utcnow()
    	timestamp=calendar.timegm(d.utctimetuple())
    	textbuffer.set_text("Humidity:\t" + humidity[-5:] +"%\n")
    	textbuffer.insert(textbuffer.get_end_iter(), 'Temperature:\t' + temperature[-5:]+"F\n")
    	textbuffer.insert(textbuffer.get_end_iter(), "Unix Timestamp:\t"+ str(timestamp))
    	print('released')
    	
    def delety(self, button):
    	#textbuffer.delete(textbuffer.get_start_iter(), textbuffer.get_end_iter())
    	textbuffer.set_text('')
    	print('Pressed to Delete')
    # Returns List
    

    def serial_com(self):
    	'''Serial communications: get a response'''

    # open serial port
        try:
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
    



builder = gtk.Builder()
builder.add_from_file("BBDisplay.glade")

textarea = builder.get_object("textview2")
window = builder.get_object("TestWindow")
txtinput = builder.get_object("entry1")
window.show_all()

m = MyScript()
handlers = {
    "onDeleteWindow": m.closeDown,
    "hello": m.printview,
    "delety": m.delety
}
builder.connect_signals(handlers)


try:
    gtk.main()
except:
    print('some error')
