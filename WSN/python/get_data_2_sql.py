import MySQLdb
import json
from datetime import datetime

def sensor1(jsonData):
    json_dict = json.loads(jsonData)
    Temp = json_dict['temp']
    Hum = json_dict['hum']
    Dust = json_dict['dust']
    Light = json_dict['light']
    Time = str(datetime.now())
    
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
    cursor = db.cursor()
    sql = "INSERT INTO sensor2 (Temp,Hum,Dust,Light,Time) VALUES (%s,%s,%s,%s,'%s')" %(Temp,Hum,Dust,Light,Time)
    try:
        cursor.execute(sql)
        db.commit()
        print("SUCCESSFUL!\n")
    except:
        print("ERROR!")
    db.close()

def sensor2(jsonData):
    json_dict = json.loads(jsonData)
    SensorID = json_dict['SensorID']
    Longl = json_dict['Long']
    Lat = json_dict['Lat']
    Time = json_dict['Time']
  
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
    cursor = db.cursor()
    sql = "INSERT INTO sensors2 (SensorID,Longl,Lat,Time) VALUES ('%s',%s,%s,'%s')" %(SensorID,Longl,Lat,Time)
    try:
        cursor.execute(sql)
        db.commit()
        print("SUCCESSFUL!\n")
    except:
        print("ERROR!")
    db.close()

def data_handle(topic, jsonData):
    if topic == "home/sensor":
        sensor1(jsonData)
    elif topic == "home/sensors2":
        sensor2(jsonData)
