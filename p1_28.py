# Write a program to find closest number to Kth index element in tuple.
def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
      
# Driver code 
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8, 10.10, 10.04] 
K = 10.05
print("List : ",lst)
print("Closest value of ",K," = ",closest(lst, K)) 