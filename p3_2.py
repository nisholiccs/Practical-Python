# A Python program to retrieve all rows from employee table and display the 
# column values in tabular form.
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="demo")
sql="SELECT * from emp;"
cur=mydb.cursor()
cur.execute(sql)
result_set = cur.fetchall()
print("Content of Employee Table\n")
for row in result_set:
	emp_id=row[0]
	emp_name=row[1]
	emp_address=row[2]
	emp_dept=row[3]
	emp_salary=row[4]
	print('%-5d %-10s %-10s %-15s %-10d'%(emp_id,emp_name,emp_address,emp_dept,emp_salary))
