# Maximum and Minimum using 3 numbers.
def max(no1, no2, no3):
	if no1 > no2 and no1 > no3:
		return no1
	elif no2 > no1 and no2 > no3:
		return no2
	else:
		return no3
def min(no1, no2, no3):
	if no1 < no2 and no1 < no3:
		return no1
	elif no2 < no1 and no2 < no3:
		return no2
	else:
		return no3

no1 = int(input("Enter Value1: "))
no2 = int(input("Enter Value1: "))
no3 = int(input("Enter Value1: "))
print("-----------------------------------")
print("Maximum Value = ",max(no1, no2, no3))
print("Minimum Value = ",min(no1, no2, no3))
