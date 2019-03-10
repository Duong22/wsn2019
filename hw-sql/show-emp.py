# Add library
import MySQLdb

# Open MySQL
db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")

# Use cursor to access 
cursor = db.cursor()

# Add values to table
sql = """select * from enterprise"""

# Execute
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for x in results:
		print(x)
except: 
	print ("Invalid database.")

# Close MySQL
db.close()
