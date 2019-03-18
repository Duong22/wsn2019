import access_table
import create_table
import table_manage


choice_1 = True
while choice_1:
	print("\n********************WELCOME TO MYSQLDB********************")
	print("1. CREATE NEW TABLE.\n2.SHOW TABLES.\n3.COPY TABLE.\n4.DELETE TABLE.\n5.SHOW DATA FROM TABLE.\n6.SHOW MAX, MIN.\n7.INSERT DATA.\n8.EXIT")
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
		name_tb = input("ENTER TABLE'S NAME: ")
		access_table.show_data(name_tb)
	elif choice_1 == "6":
		name_tb = input("ENTER TABLE'S NAME: ")
		access_table.show_max_min(name_tb)
	elif choice_1 == "7":
		name_tb = input("ENTER TABLE'S NAME: ")
		access_table.insert_value(name_tb)
	elif choice_1 == "8":
		choice_1 = None
		print ("GOOD BYE!")
	else: print ("INVALID SYNTAX. PLEASE TRY AGAIN!")



		


