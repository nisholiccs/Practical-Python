# Write a program to find the sum of dictionary keys.
def dictSum(myDict): 
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i]     
    return sum
  
dict = {'a': 100, 'b':200, 'c':300} 
print("dictionary = ",dict)
print("Sum :", dictSum(dict)) 
