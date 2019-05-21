import MySQLdb
import json

def sensor0(topic,jsonData):
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
   # cursor = db.cursor()
    if topic == "blood/bottom": 
        json_dict1 = json.loads(jsonData) 
        blood_bottom = json_dict1['blood_bottom'] 
    if topic == "blood/top":
        json_dict2 = json.loads(jsonData)
        blood_top = json_dict2['blood_top']
    print(blood_bottom,blood_top)
    #sql = "INSERT INTO sensors0 (SensorID,Temp,Hum,Longl,Lat,Time) VALUES (%s,%s,%s,%s,%s,'%s')" %(SensorID,Temp,Hum,Longl,Lat,Time)
    #try:
     #   cursor.execute(sql)
     #   db.commit()
     #   print("SUCCESSFUL!\n")
    #except:
      #  print("ERROR!")
    db.close()
   
