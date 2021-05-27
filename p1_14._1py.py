import os
fileName=input("Enter the name of the file you want to read ")

if os.path.exists(fileName):
	f=open(fileName,"r")
	print(f.readline())
	print("You can return one line by using the readline() method\n")
	print("readlines() reads the entire file until EOF \n")
	print(f.readlines())
	f.close()
else:
	print("File has been created ",fileName)
	f1=open(fileName,"x")
	f1.close()
