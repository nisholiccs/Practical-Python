# A program to create a line graph to show the profits of a company in various years.

import matplotlib.pyplot as plt
years = [2016, 2017, 2018, 2019, 2020]
profit = [853900, 865500, 876050, 885700, 844500]
plt.plot(years, profit)
plt.title("Year vs Profit in Company")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.show()
