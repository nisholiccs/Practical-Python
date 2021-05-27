'''
Write a python program to retrieve data from a file using regular expressions 
and then write that data into a file.
'''
import re
hand = open('simple.txt')
print("Content of simple.text file\n")
for line in hand:
    line = line.rstrip()
    print(line)
print("-----------------------------------------")
hand1 = open('simple.txt')
print("\nData Retrive for a word having 5 chars\n")
for data in hand1:
	data = data.rstrip()
	if re.search(r'\b\w{5}\b',data):
		print(data)