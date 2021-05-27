'''
Write a program in python to implement Salary printing file read operation. 
(File format: EmployeeNo, name, deptno, basic, DA, HRA, Conveyance) 
should perform below operations.
a)	Print Salary Slip for given Employee Number
b)	Print Employee List for Given Department Number
'''
import re
import os
size = os.path.getsize("employee.txt")
file=open("employee.txt","r")
reclen = 160
n = int(size/reclen)
empno=input("Enter Employee No:")
position = 0
found=False
for i in range(n):
    file.seek(position)
    str=file.read()
    if empno in str:
        print("-----Salary Slip------")
        print(str)

        found = True
    position+=reclen
