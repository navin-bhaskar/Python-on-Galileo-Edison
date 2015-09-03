#!/usr/bin/python

"""
This script demonstrates the usage of mraa library for configuring and
using a pin for adc operation

setup:
The LED is connected port D5 and a "Rotary angle sensor" to port A0

Demo:
start the application in the command line by using following command:
python adc.py
Rotate the rotary angle switch to control the intensity with which the 
LED glows

You can exit this demo by hitting ctrl+c

Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/04/08/python-on-intel-galileoedison-part-4-adc/

"""

import mraa
import time

PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

# Set up the PWM
pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(ADC_PIN)

while 1:
    value = adc.read()             # Read the ADC value
    led_intensity = value/ROT_MAX  # Determine the duty cycle based on ADC value
    pwm.write(led_intensity)   
    time.sleep(0.5)


