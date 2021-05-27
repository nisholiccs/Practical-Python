val1 = int(input("Enter Value1 : "))
val2 = int(input("Enter Value2 : "))

print("------Before Swap------")
print("Value of varaible 1 : ", val1)
print("Value of varaible 2 : ", val2)

val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2

print("------After Swap------")
print("Value of varaible 1 : ", val1)
print("Value of varaible 2 : ", val2)
