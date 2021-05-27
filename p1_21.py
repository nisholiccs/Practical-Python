# A program to display a pie chart showing the percentage of employees in each 
# -department of a company.
# import the pyplot library

import matplotlib.pyplot as plotter

# The slice names of a population distribution pie chart

pieLabels = 'account', 'finance', 'IT', 'HR'

# Population data

populationShare = [30, 20, 40, 10]

figureObject, axesObject = plotter.subplots()

# Draw the pie chart

axesObject.pie(populationShare,

        labels=pieLabels,

autopct='%1.2f',

startangle=90)

# Aspect ratio - equal means pie is a circle

axesObject.axis('equal')

plotter.show()
