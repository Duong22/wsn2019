import access_table
import create_table
import table_manage

def edit_table():
	choice_2 = True
	while choice_2:
		print ("AVAILABLE TABLE")
		table_manage.show_tb()
		print("1.SHOW DATA FROM TABLE.\n2.SHOW MAX, MIN.\n3.INSERT DATA.\n4.DELETE ROW.\n5.BACK.")
		choice_2 = input("SELECT YOUR CHOICE: ")
		if choice_2 == "1":
			name_tb = input("ENTER TABLE'S NAME: ")
			access_table.show_data(name_tb)
		elif choice_2 == "2":
			name_tb = input("ENTER TABLE'S NAME: ")
			access_table.show_max_min(name_tb)
		elif choice_2 == "3":
			name_tb = input("ENTER TABLE'S NAME: ")
			access_table.insert_value(name_tb)
		elif choice_2 == "4":
			name_tb = input("ENTER TABLE'S NAME: ")
			access_table.delete_data(name_tb)
		elif choice_2 == "5":
			choice_2 = None
		else: print ("INVALID SYNTAX. PLEASE TRY AGAIN!")


choice_1 = True
while choice_1:
	print("\n********************WELCOME TO MYSQLDB********************")
	print("1.3CREATE NEW TABLE.\n2.SHOW TABLES.\n3.COPY TABLE.\n4.DELETE TABLE.\n5.ACCESS TABLE\n6.EXIT")
	choice_1 = input("SELECT YOUR CHOICE: ")

	if choice_1 == "1":
		create_table.create_tb()
	elif choice_1 == "2":
		table_manage.show_tb()
	elif choice_1 == "3":
		table_manage.copy_tb()
	elif choice_1 == "4":
		table_manage.drop_tb()
	elif choice_1 == "5":
		edit_table()
	elif choice_1 == "6":
		choice_1 = None
		print ("GOOD BYE!")
	else: print ("INVALID SYNTAX. PLEASE TRY AGAIN!")
