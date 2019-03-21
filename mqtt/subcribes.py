import time
import paho.mqtt.client as mqtt
import random,json
from get_data_2_sql import sensor
from datetime import datetime

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "home/sensors"

def on_connect(client, userdata, rc):
        if rc != 0:
                pass
                print("Unable to connect to MQTT Broker,,,")
        else:
                print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_message(client, userdata, msg):
        print("MQTT Data Received...")
        print("MQTT Toic: " + msg.topic)
        print("Data: " + str(msg.payload))
        sensor(msg.payload)

client = mqtt.Client()
client.username_pw_set(username="client1",password="123456")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.subscribe(MQTT_Topic,0)
client.loop_forever()
