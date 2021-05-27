# Write a program to find N largest elements from a list.
lst = []
n = int(input("Enter No: "))
print("Enter Value: ")

for i in range(n):
	i = int(input("\t"))
	lst.append(i)

print("List data = ", lst)

def largest(lst):
	maxval = lst[0]
	for i in lst:
		if maxval < i:
			maxval = i
	print("Largest Value of list = ",maxval)

largest(lst)