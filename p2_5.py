'''
 Write a python program to create a regular expression to retrieve the 
 timings either 'am' or 'pm'.
'''
import re
s = '''Today time is 11:40 am '''
dt = re.findall(r'\s(\d{2}\:\d{2}\s?(?:AM|PM|am|pm))',s)
print("Time : ",dt)
