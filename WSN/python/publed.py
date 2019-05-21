import MySQLdb
import json
from datetime import datetime

stt=0
pwmled1=0
ktoff=1
kton=1

def pub_led1():
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
    cursor = db.cursor()
    sql = """select led1 from led1 where id = (select max(id) from led1)"""
    cursor.execute(sql)
    result = (cursor.fetchall())
    stt = result[0][0]
    return stt

def pub_pwm1():
    db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
    cursor = db.cursor()
    sql = """select led1 from controlled1 where id = (select max(id) from controlled1)"""
    cursor.execute(sql)
    result = (cursor.fetchall())
    stt = result[0][0]
    return stt

while True: 
    if(pub_led1() == 1 and ktoff == 1):
        ktoff = 0
        kton = 1
        print("LED1 ON")
    if(pub_led1() == 0 and kton == 1):
        ktoff = 1
        kton = 0
        print("LED1 OFF")
    if(pub_pwm1() != pwmled1):
        pwmled1 = pub_pwm1()
        print(pwmled1)