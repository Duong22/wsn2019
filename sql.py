# Add library
import MySQLdb

# Open MySQL
db = MySQLdb.connect("localhost","slave","123456","mangcambien2019")

# Use cursor to access 
cursor = db.cursor()

# Add values to table
sql = """insert into datasensor2(device, windspeed, light, rain) values(10, 20, 30, 40)"""

# Execute
try:
	cursor.execute(sql)
	db.commit()
except: 
	db.rollback()

# Close MySQL
db.close()
