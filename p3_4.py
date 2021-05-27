# A program to retrieve all rows from employee table and dump into CSV file.
import csv
header = ['id', 'empname' , 'gender' ,' address' , 'designation' , 'salary']
rows = [
    [1,'Rushit','male','Ahmedabad','manager',50000],
	[2,'Nishu','male','Ahmedabad','clerk',80000],
	[3,'Shreya','female','Surat','leader',45000],
	[4,'Chirag','male','Ahmedabad','analyst',30000],
	[5,'Nidhi','female','Surat','designer',40000],
	[6,'Himani','female','Porbandar','coder',34000]
]

with open('employee.csv', 'wt') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(header) 

    for row in rows:
        csv_writer.writerow(row)
print("Data inserted in csv file")