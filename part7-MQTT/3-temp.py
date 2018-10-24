#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as paho
import time
from threading import Thread
import pyupm_grove

def OnConnectHandler(client, userdata, flags, rc):
    print("Connected to the broker")

def OnDisconnecthandler(client, userdata, rc):
    print("Disconnection returned " + str(rc))

def on_message(client, userdata, message):
    info = "t: [" + message.topic + "] m: [" + str(message.payload) + "]"
    print("Message received! " + info)

def OnPublishHandler(client, userdata, mid):
    print("Message published!")

def OnSubscribeHandler(client, userdata, mid, granted_qos):
    print("Successfully subscribed! QoS: " + str(granted_qos[0]))

def publisher(client):
    time.sleep(2)
    print("Publisher task started")
    while True:
        temp = pyupm_grove.GroveTemp(1)
        print("Temperature = " + str(temp.value()))
        client.publish("temp882", str(temp.value()))
        time.sleep(5)

if __name__ == '__main__':
    client = paho.Client(client_id="65a4sd65as4dasd6", protocol=paho.MQTTv31)

    client.on_connect = OnConnectHandler
    client.on_disconnect = OnDisconnecthandler
    client.on_subscribe = OnSubscribeHandler
    client.on_publish = OnPublishHandler
    client.on_message = on_message

    host="test.mosquitto.org"
    #host="192.168.1.2"

    print("Trying to connect to " + host)
    client.connect(host, port=1883, keepalive=60, bind_address="")

    topic = "mytopic882"
    print("Subscribing to topic " + topic)
    client.subscribe(topic, qos=0)

    thread = Thread(target=publisher, args=(client,))
    thread.start()

    print("running")
    client.loop_forever()
