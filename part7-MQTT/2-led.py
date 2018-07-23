#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as paho
from time import sleep
import mraa

led = mraa.Gpio(5)        # Get the LED pin object
led.dir(mraa.DIR_OUT)     # Set the direction as output
led.write(0)

def OnConnectHandler(client, userdata, flags, rc):
    print("Connected to the broker")

def OnDisconnecthandler(client, userdata, rc):
    print("Disconnection returned " + str(rc))

def on_message(client, userdata, message):
    info = "t: [" + message.topic + "] m: [" + str(message.payload) + "]"
    print("Message received! " + info)

    if message.topic == "led6424":
        if str(message.payload) == "1":
            led.write(1)
            print("led ON")
        elif str(message.payload) == "0":
            led.write(0)
            print("led OFF")

def OnPublishHandler(client, userdata, mid):
    print("Message published!")

def OnSubscribeHandler(client, userdata, mid, granted_qos):
    print("Successfully subscribed! QoS: " + str(granted_qos[0]))

if __name__ == '__main__':
    client = paho.Client(protocol=paho.MQTTv31)

    client.on_connect = OnConnectHandler
    client.on_disconnect = OnDisconnecthandler
    client.on_subscribe = OnSubscribeHandler
    client.on_publish = OnPublishHandler
    client.on_message = on_message

    host="test.mosquitto.org"
    #host="192.168.1.2"

    print("Trying to connect to " + host)
    client.connect(host, port=1883, keepalive=60, bind_address="")

    topic = "led6424"
    print("Subscribing to topic " + topic)
    client.subscribe(topic, qos=0)

    print("running")
    client.loop_forever()
