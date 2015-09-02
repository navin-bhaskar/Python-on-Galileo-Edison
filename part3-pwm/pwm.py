#!/usr/bin/python

import mraa
import time


pwm = mraa.Pwm(5)
pwm.enable(True)
value = 0

pwm.period_us(5000);

delta = 0.05

while 1:
    
    if (value >= 1):
        value = 1
        delta = -0.05
    elif (value <=0):
        value = 0
        delta = 0.05

    pwm.write(value)
    
    value = value + delta

    time.sleep(0.5)
    
    

