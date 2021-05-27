# Write a program to calculate standard deviation of a dictionary in Python.
import statistics 
  
# creating a simple data - set 
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print("List of Sample : ",sample)
print("--------------------------------------------------")
print("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample))) 