#!/usr/bin/python

import mraa 
import time

"""
This script demonstrates the usage of mraa library for configuring and
using a GPIO as input port

setup:
The LED is connected port D5 and button is connected to port D6

Demo:
start the application in the command line by using following command:
python button.py
Press the button to toggle the LED from off to on, on to off...

You can exit this demo by hitting ctrl+c

Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/04/06/python-on-intel-galileoedison-part-2-buttons/


"""

LED_GPIO = 5                   # The LED pin
BUTTON_GPIO = 6                # The button GPIO
led = mraa.Gpio(LED_GPIO)      # Get the LED pin object
led.dir(mraa.DIR_OUT)          # Set the direction as output
ledState = False               # LED is off to begin with
led.write(0)

btn = mraa.Gpio(BUTTON_GPIO)
btn.dir(mraa.DIR_IN)

def getButtonPress():
    
    while 1:
        
        if (btn.read() != 0):
            continue
        else:
            time.sleep(0.05)
            if (btn.read() == 1):
                return
            else:
                continue

while 1:
    
    getButtonPress()
    if ledState == True:
        led.write(1)
        ledState = False
    else:
        led.write(0)
        ledState = True

    time.sleep(0.005)
