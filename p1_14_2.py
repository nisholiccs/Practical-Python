import os
fileName=input("Enter the name of the file you want to write in : ")


if os.path.exists(fileName):
	f1=open(fileName,"a")
	str=input("Enter contents you want to write into the file using write() :  ")
	f1.write(str)

	f1.write("\n")
	print(str,'written in file successfully \n \n')
	print('List of numbers : ["1","2","3","4","5"] written using writelines() function')
	list=["1","2","3","4","5"]
	f1.write("\n")
	f1.writelines(list)
	f1.close()
else:
	print("File doesn't exist")
