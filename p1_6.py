# Find Maximum Odd Number in the List
def findOdd(no):
	for i in no:
		if i % 2 != 0:
			odd.append(i)
	print("Odd No's = ",odd)

def findOddMax(odd):
	for i in odd:
		value = odd[0]
		if value < i:
			value = i
	print("Maximum Odd Number : ", value)

no = []
odd = []
for i in range(10):
	val = int(input("Enter value : "))
	no.append(val)
findOdd(no)
findOddMax(odd)