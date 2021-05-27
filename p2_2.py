'''
2.2. Create utility script to process telephone numbers such that
a. Area codes (the first set of three-digits and the accompanying hyphen) 
	are optional, that is, your regex should match both 800-555-1212 as well 
	as just 555-1212.
b. Either parenthesized or hyphenated area codes are supported, 
	not to mention optional; make your regex match 800-555-1212, 555-1212, 
	and also (800) 555-1212.
'''
import re 

# Option a)
phoneNumRegex = re.compile(r'(\(\d\d\d\) ||(\d\d\d\-))*(\d\d\d-\d\d\d\d)') 
print("------------------------------------")
print("\t\tOption A")
print("------------------------------------")
mo = phoneNumRegex.search('My number is 800-555-1212.') 
no = phoneNumRegex.search('My number is 555-1212.')
print('Phone Number: ' + mo.group()) 
print('Phone Number: ' + no.group())
print("------------------------------------")
# Option b)
print("\t\tOption B")
print("------------------------------------")
s = phoneNumRegex.search('My phone number is (800) 555-1212.')
print("Phone Number:" + s.group())
print("------------------------------------")
