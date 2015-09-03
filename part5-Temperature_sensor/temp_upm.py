#!/usr/bin/python

"""
This script demonstrates the usage of upm library for interfacing a 
temperature sensor

setup:
The temperature sensor is connected to port A1

Demo:
start the application in the command line by using following command:
python temp_upm.py
You should see the temperature being printed out in the console

Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/04/09/python-on-intel-galileoedison-part-5temperature-sensor-with-mraa-and-upm/

"""


import pyupm_grove # Get the UPM library

# Create the temperature sensor object
temp = pyupm_grove.GroveTemp(1)

# Use "value" method on it to get the temperature
print "Temperature now is " + str(temp.value())
