# Write a program to remove empty tuples from a list.
def remove(tuples): 
    # tuples = filter(None, tuples) 
    tuples = [t for t in tuples if t] 
    return tuples 
  
# Driver Code 
t1 = [(), ('rushit','15','8'), (), ('nishu', 'shreya'),  
          ('himani','nidhi'), ('',''),()] 
print(remove(t1))