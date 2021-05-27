# Write a program to find maximum and minimum K elements in Tuple.
# initialize list  
test_list = [(2, 4), (60, 7), (5, 90), (100, 10), (88, 7)] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# Maximum element in tuple list 
# using max() + generator expression 
res = max(int(j) for i in test_list for j in i) 
  
# printing result 
print("The Maximum element of list is : " + str(res))