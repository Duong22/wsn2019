import time
import paho.mqtt.client as mqtt
import random,json
from datetime import datetime

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic1 = "home/sensor2"
MQTT_Topic2 = "test"


def on_connect(client, userdata, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker,,,")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
    pass

def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username="client1", password="123456")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

def pusblish_2_topic(topic, message):
    mqttc.publish(topic,message)
    print(("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic)))
    print("")

def publish_fake_sensor1_values_2_MQTT():
    Temp_fake_value = int(random.randint(10, 40))
    Hum_fake_value = int(random.randint(50, 100))
    dust_fake_value = float(round(random.uniform(0, 1),2))
    light_fake_value = int(random.randint(100, 900))
    Sensor_data = {}
    Sensor_data['temp'] = Temp_fake_value
    Sensor_data['hum'] = Hum_fake_value
    Sensor_data['dust'] = dust_fake_value
    Sensor_data['light'] = light_fake_value
    Sensor_data['Time'] = str(datetime.now())
    sensor_json_data = json.dumps(Sensor_data)
    print("Publishing fake Sensor data: ")
    pusblish_2_topic(MQTT_Topic1, sensor_json_data)

def publish_fake_sensor2_values_2_MQTT():
    Sensor_data = {}
    Sensor_data['SensorID'] = int(random.randint(1,5))
    if (Sensor_data['SensorID'] == 1):
        Sensor_data['Long'] = 1000
        Sensor_data['Lat'] = 500
    elif (Sensor_data['SensorID'] == 2):
        Sensor_data['Long'] = 600
        Sensor_data['Lat'] = 700
    elif (Sensor_data['SensorID'] == 3):
        Sensor_data['Long'] = 800
        Sensor_data['Lat'] = 400
    elif (Sensor_data['SensorID'] == 4):
        Sensor_data['Long'] = 300
        Sensor_data['Lat'] = 100
    elif (Sensor_data['SensorID'] == 5):
        Sensor_data['Long'] = 900
        Sensor_data['Lat'] = 200
    Sensor_data['Time'] = str(datetime.now())
    print("Publishing fake Sensor data: ")


while True:
    publish_fake_sensor1_values_2_MQTT()
    publish_fake_sensor2_values_2_MQTT()
    time.sleep(3)