# - A program to read CSV file and upload data into table.
import csv

with open('demo1.csv', 'rt') as f:
    csv_reader = csv.reader(f)

    for line in csv_reader:
        print(line[0], line[1], line[2])
print("Data Inserted")

# import pandas as pd
# import csv
# import mysql.connector

# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="root",
# 	database="demo")
# filename = "demo1.csv"
# fields = []
# rows = []
# with open(filename,'r') as file:
# 	fields = next(csvreader)
# 	for row in csveader:
# 		rows.append(row)
# 	print("Total no of rows : %d"%(csvreader.line_num))
# 	print('Field names are:' + ', '.join(field for field in fields)) 
# 	print('\nFirst 5 rows are:\n') 
# cur = mydb.cursor()
# # qry = "insert into demo1 ('No', 'Name', 'Age') values (%d,%s,%s)"
# # with open('demo1.csv', mode ='r')as file: 
# # 	csvFile = csv.reader(file) 
# # 	lst = []
# # 	for lines in csvFile: 
# # 		print(lines)
# #         lst.append(lines)

# # cur.executemany(qry,lst)
# # print("Data Susccessfully Filled")

