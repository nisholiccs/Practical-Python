# A program to create a line graph to show the profits of a company in various years.

import matplotlib.pyplot as plt

year = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
profit = [100000, 50000, 40000, 80000, 88000, 10000, 90000]
plt.plot(year, profit, color='r')
plt.xlabel('years')
plt.ylabel('profit')
plt.title('profit of company')
plt.show()	