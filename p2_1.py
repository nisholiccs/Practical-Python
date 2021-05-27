'''
2.1. Create Regular Expressions that
a) Recognize following strings bit, but, bat, hit, hat or hut
b) Match any pair of words separated by a single space, that is, first and last names.
c) Match any word and single letter separated by a comma and single space,
	as in last name, first initial.
d) Match simple Web domain names that begin with www and end with a ".com" suffix;
	for example, www.yahoo.com. Extra Credit: If your regex also supports other 
	high-level domain names, such as .edu, .net, etc. (for example: www.foothill.edu).
e) Match a street address according to your local format 
	(keep your regex general enough to match any number of street words, 
	including the type designation). 
	For example, American street addresses use the format: 1180 Bordeaux Drive. 
	Make your regex flexible enough to support multi-word street names such as: 3120 
	De la Cruz Boulevard.
'''
import re
pattern = '[bh][aiu]t'
text = 'rushit'
m = re.search(pattern, text)
if m is not None:
	print("Data = ",m.group())
pattern = '[a-zA-Z]+ [a-zA-Z]+'
text = 'Nishu Bhardwaj'
m = re.match(pattern, text)
if m is not None:
	print("Data = ",m.group())
pattern = '([A-Z]\. )+[A-Za-z]+'
text = 'n. s'
m = re.match(pattern, text)
if m is not None:
	print(m.group())
pattern = 'w{3}(\.[\w_]+)+((\.com)|(.edu)|(.net))'
text = 'www.foothill.edu'
m = re.search(pattern, text)
if m is not None:
	print("Website = ",m.group())
pattern = r'\d{4} ([a-zA-Z]+ )+[a-zA-Z]+'
text = '3120 De la Cruz Boulevard'
m = re.search(pattern, text)
if m is not None:
	print("String = ",m.group())
