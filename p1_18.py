'''
Write a program in python to implement Bank System using Class and Methods and
perform below operations. (Note: Use of object oriented paradigm is compulsory.)
a)	Add Bank account
b)	Deposit of money
c)	withdrawal operation
d)	Money transfer
e)	Show Balance
'''
import datetime

class account:
	accountName=""
	accountNumber=0
	accountBalance=0.0
	accounttype=""
	
	def __init__(self,aname,anum,abal,atype):
		self.accountName=aname
		self.accountNumber=anum
		self.accountBalance=abal
		self.accounttype=atype
	def deposite(self,amt):
		self.accountBalance += amt
		return self.accountBalance
	def withdraw(self,amt):
		self.accountBalance -= amt
		return self.accountBalance
	def transfer(self,ac,amt):
		self.accountBalance += amt
		ac.accountBalance -= amt

a=[]																	
a.append(account('Rushit',5764990907,200000,'saving'))
a.append(account('Nishu ',576499870,150000,'saving'))
a.append(account('Shreya',923190907,200000,'current'))

print('Main Balance')
print(a[0].accountName,"Account Balance ","",a[0].accountBalance)	
print(a[1].accountName,"Account Balance ","",a[1].accountBalance)	
print(a[2].accountName,"Account Balance ","",a[2].accountBalance)	


print("\n")
print('Add Deposit Amount')
print(a[0].accountName,"",a[0].deposite(200000))
print(a[1].accountName,"",a[1].deposite(250000))
print(a[2].accountName,"",a[2].deposite(150000))


print("\n")
print('Withdraw Amount')
print(a[0].accountName,"",a[0].withdraw(20000))
print(a[1].accountName,"",a[1].withdraw(15000))	
print(a[2].accountName,"",a[2].withdraw(10000))


print("\n")
a[0].transfer(a[1],2000)

print(a[1].accountName," tranfer 2000 to","",a[0].accountName)

print("\n")
print(a[0].accountName,"Account Balance ","",a[0].accountBalance)
print(a[1].accountName,"Account Balance ","",a[1].accountBalance)	
