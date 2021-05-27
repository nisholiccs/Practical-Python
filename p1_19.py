# A Python program to display employee id numbers on X-axis and their salaries 
# on Y-axis in the form a bar graph.
import matplotlib.pyplot as plt
import pandas as pd
empdata={"empid":[101,102,103,104,105],"ename":["Rushit","Nishu","Shreya","Himani","Nidhi"],"sal":[50000,45000,20000,30000,20000],"doj":["1-1-2017","15-1-2017","23-12-2017","20-7-2016","16-8-1995"]}
df=pd.DataFrame(empdata)
x=df['empid']
y=df['sal']
plt.bar(x,y, label='Employee data',color='red')
plt.xlabel('Employee ids')
plt.ylabel('Employee salaries')
plt.title('MICROSOFT INC')
plt.legend()
plt.show()
