# Write a program to extract digits from string.
test_string = input("Enter String: ")
print("The original string : " + test_string)   
res = ''.join(filter(lambda i: i.isdigit(), test_string)) 
print("The digits string is : " + str(res)) 