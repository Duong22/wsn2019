import MySQLdb

db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
cursor = db.cursor()
sql = """CREATE TABLE datasensor6(ID int(10) primary key auto_increment, SensorID char(10) not null, Temp int(10) not null, Hum int(10) not null, Time datetime)"""
try:
    cursor.execute(sql)
    print("Successful!")
except:
    print("Error!")