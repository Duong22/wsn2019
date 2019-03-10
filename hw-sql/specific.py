# Add library
import MySQLdb

# Open MySQL
db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")

# Use cursor to access 
cursor = db.cursor()

# Ask info about the employee
name = input("Enter employee's name: ")

# Add values to table
sql = """select * from enterprise where Name = '%s'""" % (name)

# Execute
try:
	cursor.execute(sql,)
	results = cursor.fetchall()
	for x in results:
		print(x)
except: 
	print ("Invalid database.")

# Close MySQL
db.close()
