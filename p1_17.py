'''
	Write a program in python to implement Library Management System using file handling
	technique. System should perform below operations.
	a)	Issue a book for student.
	b)	List information today's issued books.
	(Note: Use of object oriented paradigm is compulsory.)
'''
import datetime

class book:
	bname=""
	bid=0

	def __init__(self,b_name,b_id):
		self.bname = b_name
		self.bid = b_id
		issuedate = ""
		sname = ""

	def show(self):
		print("bookname ",self.bname,"bookid ",self.bid)
		
	def issue_book(self,issue,to):
		self.issuedate=issue
		self.sname=to
	
now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

bookarray=[]
bookarray.append(book("Python",5674))
bookarray.append(book("DBMS",9843))
bookarray.append(book("Java",9023))
bookarray.append(book("Maths",3210))

bookarray[0].issue_book(str(now),'Rushit')
bookarray[1].issue_book(str(now),'Nishu')
bookarray[2].issue_book(str(now),'Shreya')
bookarray[3].issue_book('2019-11-07 13:48:12','Rushit')
	
dt = datetime.datetime.strptime(bookarray[2].issuedate,'%Y-%m-%d %H:%M:%S')

for i in bookarray:
	dt = datetime.datetime.strptime(i.issuedate,'%Y-%m-%d %H:%M:%S')
	dt2 = datetime.datetime.strptime(str(now),'%Y-%m-%d %H:%M:%S')

	if(dt.date()==dt2.date()):
		print(i.bname)
