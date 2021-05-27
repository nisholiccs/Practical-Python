# Calculator using function.
def add(a, b):
	return a + b
def sub(a, b):
	return a - b
def mul(a, b):
	return a * b
def div(a, b):
	return a / b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch = input("Enter choice(1/2/3/4): ")
print("------------------------------")
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
if ch == '1':
	print("Addition of ",a, " + ",b, " = ",add(a,b))
elif ch == '2':
	print("Subtraction of ",a, " - ",b, " = ",sub(a,b))
elif ch == '3':
	print("Multiplication of ",a, " * ",b, " = ",mul(a,b))
elif ch == '4':
	print("Division of ",a, " / ",b, " = ",div(a,b))
else:
   print("Invalid Input")



