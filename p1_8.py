# Palindrome
no = int(input("Enter Number : "))
tmp = no
val = 0

while no > 0:
	val = (val * 10) + (no % 10)
	no = no // 10

if tmp == val:
	print(tmp," is Palindrome")
else:
	print(tmp, "is not Palindrome")
