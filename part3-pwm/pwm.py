#!/usr/bin/python

import mraa
import time

"""
This script demonstrates the usage of mraa library for configuring and
using a pin as PWM

setup:
The LED is connected port D5

Demo:
start the application in the command line by using following command:
python pwm.py
The LED would start with off state then gradually increases it's 
intensity to maximum and then decreses it's intensity until it turns off
and repeats the cycle.

You can exit this demo by hitting ctrl+c

Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/04/07/python-on-intel-galileoedison-part-3-pwm/

"""

PWM_PIN = 5
pwm = mraa.Pwm(PWM_PIN)


"""
Control the period with "period_us"

            +----------------+                +----------------+                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            |                |                |                |                |
            +                +----------------+                +----------------+
            ^                                 ^
            |                                 |
            |<---------- Period ------------->|
            |               ^                 |
            |               |                 |
                            | 
            pwm.period_us(5000)
  
"""  

pwm.period_us(5000)        # Set the period as 5000 us or 5ms

pwm.enable(True)           # enable PWM
value = 0

delta = 0.05               # Used to manipulate duty cycle of the pulse

while 1:
    
    if (value >= 1):
        # Itensity at max, need to reduce the duty cycle, set -ve delta
        value = 1
        delta = -0.05
    elif (value <=0):
        value = 0
        # Intensity at lowest, set a +ve delta
        delta = 0.05
        
    """
    Control the duty cycle with "write"
            +------+                            +------+                            
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            |      |                            |      |                           
            +      +----------------------------+      +---------------------------+
            ^      ^
            |      |
            |<---->|
                ^
                |
                |
     pwm.write(0.2)
    """
    
    pwm.write(value) # Set the duty cycle
    
    value = value + delta

    time.sleep(0.5)
    
    

