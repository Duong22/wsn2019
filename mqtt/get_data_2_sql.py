import MySQLdb
import json

def sensor(jsonData):
    json_dict = json.loads(jsonData)
    SensorID = json_dict['SensorID']
    Temp = json_dict['Temp']
    Hum = json_dict['Hum']
    Time = json_dict['Time']
  
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
    cursor = db.cursor()
    sql = "INSERT INTO datasensor6 (SensorID,Temp,Hum,Time) VALUES ('%s',%s,%s,'%s')" %(SensorID,Temp,Hum,Time)
    try:
        cursor.execute(sql)
        db.commit()
        print("SUCCESSFUL!\n")
    except:
        print("ERROR!")
    db.close()