import MySQLdb

db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
cursor = db.cursor()
sql1 = """CREATE TABLE sensor2(ID int(10) primary key auto_increment, Temp int(10) not null,Hum int(10) not null, Dust float(10) not null, Light int(10) not null, Time datetime)"""
try:
    cursor.execute(sql1)
    print("Successful!")
except:
    print("Error!")
sql2 = """CREATE TABLE led1(ID int(10) primary key auto_increment, led1 int(10) not null)"""
try:
    cursor.execute(sql2)
    print("Successful!")
except:
    print("Error!")
sql3 = """CREATE TABLE controlled1(ID int(10) primary key auto_increment, led1 int(10) not null)"""
try:
    cursor.execute(sql3)
    print("Successful!")
except:
    print("Error!")


