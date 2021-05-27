# A program to display a histogram showing the number of employees in specific age groups.
import matplotlib.pyplot as plt
emp_ages=[22,45,30,29,38,32,57,45,43,43,50,40,34,33,25,19,27,29,31,35,45,]
bins=[0,10,20,30,40,50,60]
plt.hist(emp_ages,bins,histtype='bar',rwidth=0.8,color='orange')
plt.xlabel('Employee ages')
plt.ylabel('no. of employees')
plt.title('ORACLE CORP')
plt.legend()
plt.show()
