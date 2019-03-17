import menu
import table_manage
import access_table
import MySQLdb

db = MySQLdb.connect("localhost","boss","123456","mangcambien2019")
cursor = db.cursor()

sql = """SELECT * from datasensor2"""

cursor.execute(sql)
results = cursor.description
print(results)

