import MySQLdb

def show_data(name_tb):
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
	cursor = db.cursor()

	sql = """SELECT * from %s""" % (name_tb)

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
def show_max_min(name_tb):
	db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
	cursor = db.cursor()
	name_tb = input("ENTER TABLE'S NAME: ")
	name_col = input("ENTER COLUMN'S NAME: ")
	sql = """SELECT MIN(%s) FROM %s; SELECT MAX(%s) FROM %s"""(name_col,name_tb,name_col,name_tb)
	curosr.execute(sql)
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

#def insert_value(name_tb):
	
	
