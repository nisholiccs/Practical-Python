'''
Create Web Database Application “Address Book” with options to
a) add/ insert a record ,
b) modify a record ,
c) display a record
d) delete a record
'''
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="demo")
print("\n----------MENU----------\n")
print("1. ADD RECORD")
print("2. MODIFY RECORD")
print("3. DISPLAY RECORD")
print("4. DELETE RECORD")
print("5. EXIT")
i = input("Enter your Choice: ")
while i >= '1' and i <= '5':
	if i == '1':
		id = input("Enter the P_ID: ")
		name = input("Enter the name: ")
		add = input("Enter the address: ")
		qry="insert into Address_Book (P_ID, name, address) values("+id+", \'"+name+"\', \'"+add+"\');"
		try:
			cur=mydb.cursor()
			cur.execute(qry)
			mydb.commit()
			print ("one record added successfully")
		except:
			print ("error in operation")
			mydb.rollback()

	if i == '2':
		id=input("Enter the id to be updated: ")
		name=input("Enter the new updated name: ")
		qry="update Address_Book set name=\'"+name+"\' where P_ID="+id+";"
		try:
			cur=mydb.cursor()
			cur.execute(qry)
			mydb.commit()
			print("record updated successfully")
		except:
			print("error in operation")
			mydb.rollback()
	if i == '3':
		sql="SELECT * from Address_Book"
		cur=mydb.cursor()
		cur.execute(sql)
		while True:
			record=cur.fetchone()
			if record==None:
				break
			print (record)
	if i == '4':
		id = input("Enter the id to be deleted: ")
		qry="DELETE from Address_Book where P_ID="+id+";"
		try:
			cur=mydb.cursor()
			cur.execute(qry)
			mydb.commit()
			print("record deleted successfully")
		except:
			print("error in operation")
			mydb.rollback()
	if i == '5':
		exit()
	i = input("\nEnter your choice: ")
else:
	print("Invalid Choice")
mydb.close()
