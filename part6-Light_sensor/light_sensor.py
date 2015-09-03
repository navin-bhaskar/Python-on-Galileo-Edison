#!/usr/bin/python


import pyupm_grove
import mraa
import time
import sys

"""
This script demonstrates the usage of the light sensor using upm

setup:
The light sensor is connected to port A0 and an LED is connected to port
D5.

Demo:
start the application in the command line by using following command:
python light_sensor.py
While running the demo, you should see a bar appear in the console whose
length ins controlled by the intensity of the ambient light and also 
the LED connected at port D5 should light more brightly if the 
intensity of the ambient light is less and vice versa.

You can exit this demo by hitting ctrl+c

"""

LIGHT_SENSOR_PIN=0         # Analog input port where the the light sensor is connected
MAX_LIGHT = 50
LED_PWM_PIN=5

def main():
    light = pyupm_grove.GroveLight(LIGHT_SENSOR_PIN)
    pwm = mraa.Pwm(LED_PWM_PIN)
    pwm.period_us(5000) # Set the period as 5000 us or 5ms
    pwm.enable(True)    # enable PWM
    pwm.write(0)
    print "Light sensor bar:"
    while True:
        ambientLight = light.value()
        sys.stdout.write("Light sensor: %02d " %ambientLight)
        sys.stdout.write("[")
        # Control the intensity of the LED connected to PWM depending on the 
        # intensity of the ambient light, if intensity is more, the LED will light less brightly
        tempLight = ambientLight
        if tempLight > MAX_LIGHT:
            tempLight = MAX_LIGHT      # Nromalize the value
            
        pwmValue = (MAX_LIGHT - tempLight)/float(MAX_LIGHT)

        pwm.write(pwmValue)
        
        for i in range(0, MAX_LIGHT):
            if ambientLight > i:
                sys.stdout.write("=")
            elif ambientLight == i:
                sys.stdout.write("|")
            else:
                sys.stdout.write(" ")
                
        #sys.stdout.write("] pwm:%f\r" %pwmValue) # un comment this line if you want to see PWM value
        sys.stdout.write("]  \r")
        sys.stdout.flush()
        time.sleep(0.1)


    
if __name__ == "__main__":
    main()
