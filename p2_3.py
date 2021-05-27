'''
2.3 Write a python program to create a regular expression to retrieve 
all words having 5 characters length.
'''
import re
text = '''"Hello World Apple Banana readme"'''
print("String = ",text)
print("--------------------------------------------------------")
print("Words having 5 characters = ",re.findall(r"\b\w{5}\b",text))