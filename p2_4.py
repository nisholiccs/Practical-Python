'''
 Write a python program to create a regular expression to retrieve all words
 starting with 'a' in a given string.
'''
import re

text = "Apple aman Rushit Abu aap "
print("String = ",text)
print("-------------------------------")
list = re.findall("[a]\w+", text)
print("List start with 'a' = ",list)