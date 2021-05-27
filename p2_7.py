'''
Write a python program to retrieve information from a HTML file using a 
regular expression.
'''
# import urllib.request, urllib.parse, urllib.error
# import re

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# links = re.findall(b'href=\"(http://.*?)\"', html)
# for link in links:
#     print(link.decode())

import re
import urllib.request
# open the html file using urlopen() method
f = urllib.request.urlopen(r'file:///e|mca\Sem3\Rushit\Syllabus\breakfast.html')
# read data from the file object into text string
text = f.read()
# convert the byte string into normal string
str = text.decode()
# apply regular expression on the string
result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>', str)
# display result
print(result)
# display the items of the result
for item, price in result:
	print('\n\tItem= %-15s Price= %-10s' %(item, price))
# close the file
f.close()
