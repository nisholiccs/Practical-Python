## Write a Python program to perform following operation on given string input: 
## a) Count Number of Vowel in given string
## b) Count Length of string (donot use len() )
## c) Reverse string
## d) Find and replace operation
## e) check whether string entered is a palindrome or not 

print("1. Count Number of Vowel in given string")
print("2. Count Length of string (donot use len())")
print("3. Reverse string")
print("4. Find and replace operation")
print("5. check whether string entered is a palindrome or not\n")
# print("Enter your choice : ")
ch = int(input("Enter your choice : "))

def strval(valstr):
    total=0
    for i in valstr:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            total = total + 1
    return total

def lenstr(valstr):
    total=0
    for i in valstr:
        total = total + 1
    return total

def revstr(valstr):
    return valstr[::-1]
def findstr(valstr):
    pass

if(ch==1):
    valstr = input("Enter the String : ")
    print("Number of Vowel string => ",strval(valstr))
elif(ch == 2):
    valstr = input("Enter the String : ")
    print("length of string => ",lenstr(valstr))
elif(ch == 3):
    valstr = input("Enter the String : ")
    print("Reverse string => ",revstr(valstr))
elif(ch == 4):
    valstr = input("Enter the String : ")
    print("Find string => ",findstr(valstr))
elif(ch == 5):
    valstr = input("Enter the String : ")
    if valstr == revstr(valstr):
        print(valstr," is Palindrome")
    else:
        print(valstr," is not Palindrome")
else:
    print("Invalid Option")
