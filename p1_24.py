# prime using function
def prime(no):
	flag = 0
	if no >= 1 :
		for i in range(2,no) :
			if no % i == 0 :
				flag = 1
	else :
		print(no,"is not prime")
	if flag == 1 :
		print(no," is not prime")
	else :
		print(no," is prime")

no = int(input("Enter Number: "))
prime(no)
