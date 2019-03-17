# Add library
import MySQLdb

def create_tb():
	name_tb = input("Table's name: ")
	num_column = int(input("Number of column: "))
	column = ""
	for i in range(0, num_column):
		name_column = input("Name column %s: " % (i+1))
		data_type = input("Data type column %s: " % (i+1))
		column = column + name_column + " " + data_type + " not null, " 
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
	cursor = db.cursor()
	sql = """CREATE TABLE %s(id int(10) primary key auto_increment, %s time datetime);""" % (name_tb, column)
	try:
		cursor.execute(sql)
		print("SUCCESS!")
	except: 
		print ("ERROR!")

	db.close()


