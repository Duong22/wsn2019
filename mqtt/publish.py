import time
import paho.mqtt.client as mqtt
import random,json
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

def publish_fake_sensor_values_2_MQTT():
    Hummidity_fake_value = int(random.randint(50, 100))
    Temparature_fake_value = int(random.randint(20, 30))
    Sensor_data = {}
    Sensor_data['SensorID'] = "DHT-11"
    Sensor_data['Temp'] = Temparature_fake_value
    Sensor_data['Hum'] = Hummidity_fake_value
    Sensor_data['Time'] = str(datetime.now())
    sensor_json_data = json.dumps(Sensor_data)
    print("Publishing fake Sensor data: ")
    pusblish_2_topic(MQTT_Topic, sensor_json_data)

while True:
    publish_fake_sensor_values_2_MQTT()
    time.sleep(3)