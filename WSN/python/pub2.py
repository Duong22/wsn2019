import paho.mqtt.client as mqtt
import random
import json
from datetime import datetime
from time import sleep
import MySQLdb

Broker = "localhost"
Port = 1883
Wait = 45
Topic = "sttled"
stt=3
kton = 1
ktoff = 1
pwmled1 = 0


def on_connect(client, userdata, flags, rc):
    if rc!= 0:
        pass
        print('Unable to connect to Broker...')
    else:
        print('Connected with Broker: ' + str(Broker))

def on_publish(client, userdata, mid):
    pass

def disconnect(client, userdata, rc):
    if rc != 0:
        pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username = "client1", password = "123456")
mqttc.on_connect = on_connect
mqttc.disconnect = disconnect
mqttc.on_publish = on_publish
mqttc.connect(Broker, Port, Wait)

def pub2topic(topic, message):
    mqttc.publish(topic,message)
    print(('Published: ' + str(message) + ' ' + 'on MQTT topic: ' + str(topic)))
    print('')

def pub_data_fake():
    db = MySQLdb.connect("localhost","tuananh","abc13579","wordpress")
    cursor = db.cursor()
    sql = """select led1 from led1 where id = (select max(id) from led1)"""
    cursor.execute(sql)
    result = (cursor.fetchall())
    stt = result[0][0]
    return stt

def pub_pwm1():
    db = MySQLdb.connect("localhost","tuananh","abc13579","wordpress")
    cursor = db.cursor()
    sql = """select led1 from controlled1 where id = (select max(id) from controlled1)"""
    cursor.execute(sql)
    result = (cursor.fetchall())
    stt = result[0][0]
    return stt

while True:
    if(pub_data_fake() == 1 and ktoff == 1):
        mqttc.publish(Topic,"led1on")
        ktoff = 0
        kton = 1
        print("LED1 ON")
    if(pub_data_fake() == 0 and kton == 1):
        mqttc.publish(Topic,"led1off")
        ktoff = 1
        kton = 0
        print("LED1 OFF")
    if(pub_pwm1() != pwmled1):
        pwmled1 = pub_pwm1()
        mqttc.publish("led1pwm",str(pwmled1))
