#!/usr/bin/python

"""
This script demonstrates the usage of mraa library for interfacing a 
temperature sensor

setup:
The temperature sensor is connected to port A1

Demo:
start the application in the command line by using following command:
python temp_mraa.py
You should see the temperature being printed out in the console

Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/04/09/python-on-intel-galileoedison-part-5temperature-sensor-with-mraa-and-upm/

"""
import mraa
import time
import math

# More info on Temperature sensor here -> http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor

B=3975
ain = mraa.Aio(1)
a = ain.read()
resistance = (1023-a)*10000.0/a
temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
print "Temperature now is " + str(temp)
