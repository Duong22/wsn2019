# Add library
import MySQLdb

# Add information
name = input("Enter employee's name: ")
ID = 'asdf'#input("Enter employees's ID-Number: ")
salary = input("Enter employees's salary: ")

# Open MySQL
db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")

# Use cursor to access 
cursor = db.cursor()

# Add values to table
sql = """insert into enterprise(Name, Salary) values('%s', '%s')""" % (name, salary)

# Execute
try:
	cursor.execute(sql)
	db.commit()
	print('Updated!')
except: 
	db.rollback()

# Close MySQL
db.close()


