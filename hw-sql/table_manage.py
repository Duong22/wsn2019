# Add library
import MySQLdb

def show_tb():
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019") 
	cursor= db.cursor()
	sql = "SHOW TABLES;"
	cursor.execute(sql)
	results = cursor.fetchall()

	widths = []
	columns = []
	tavnit = '|'
	separator = '+' 

	for cd in cursor.description:
	    widths.append(max(cd[2], len(cd[0])))
	    columns.append(cd[0])

	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'

	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)
	db.close()
def copy_tb():
	av_tb = input("ENTER THE TABLE YOU WANT TO COPY: ")
	new_tb = input("ENTER NEW NAME FOR THE DUPLICATE TABLE: ")
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019") 
	cursor= db.cursor()
	sql = "CREATE TABLE %s as select * from %s" % (new_tb, av_tb)
	try:
		cursor.execute(sql)
		print("SUCCESSFUL!")
	except:
		print("ERROR!")
def drop_tb():
	tb = input("ENTER THE TABLE YOU WANT TO DELETE: ")
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019") 
	cursor= db.cursor()
	sql = "DROP TABLE %s;" % (tb)
	try:
		cursor.execute(sql)
		print("SUCCESSFUL!")
	except:
		print("ERROR!")
	
