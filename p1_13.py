import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class simpleInterest:	
	def __init__(self,p,rateOfInterest,term):
		self.p=p
		self.rateOfInterest=rateOfInterest
		self.term=term

	def display(self):
		print ("Principal",self.p)

	def calculateInterest(self):
		i=self.p*self.rateOfInterest*self.term
		return i

	def getPrincipal():
		return p
			
class compoundInterest(simpleInterest):
	def __init__(self,principal,rateOfInterest,term,ntimes=1):
		super().__init__(principal,rateOfInterest,term)
		self.ntimes=ntimes		

	def calculateCompoundInterest(self):
		a=self.p*(pow((1+self.rateOfInterest/self.ntimes),self.term))
		return a

s1=simpleInterest(20000,3.5,5)
i=s1.calculateInterest()

c1=compoundInterest(20000,1,5)
j=c1.calculateCompoundInterest()
		
objects = ('Simple Interest', 'Compound Interest')
y_pos = np.arange(len(objects))
performance = [i,j]

plt.bar(y_pos, performance, align='center', alpha=0.5,width=0.35)
plt.xticks(y_pos, objects)
plt.xlabel('Interest')
plt.title('Interest difference for the term of 5 years')
plt.show()
