# '''
# Write a program in python to implement Railway Reservation System using file handling technique.
# System should perform below operations. (Note: Use of object oriented paradigm is compulsory.)
# a)	Reserve a ticket for a passenger.
# b)	List information all reservations done for today’s trains.
# '''

import sys

class Railway:

    user=[['rushit',1111],['nishu',2222],['shreya',3333],['himani',4444]]

    def login(self,username,pin):

        if [username,pin] in Railway.user:
            print('\n')
            print('Welcome user:',username)
        else:
            print("Username or Password wrong:")
            sys.exit(0)

    def reservation(self,train,date,train_class,starting_From,destination):
         filehandle = open("Railway_Reservation.txt","w")
         filehandle.write("You Selected Train is       : "+train)   
         filehandle.write("\nYour Journy dateis        : "+date)
         filehandle.write("\nYour Train class is       : "+train_class)
         filehandle.write("\nYour Journy starting From : "+starting_From)
         filehandle.write("\nYour Destination is       : "+destination)
         filehandle.close()
         print("Your Ticket Booked")

    def showtrains(self):
        file = open("Railway_Reservation.txt","r")
        str=file.read()
        print("---------------Reserved Train---------------")
        print(str)

Rail = Railway()
print("**********Welcome to Railway**********")
username=input("Enter User Name:")
pin=int(input("Enter Your Pin:"))
Rail.login(username,pin)

while(True):

    print('\n')
    print("**********Railway Reservation**********")
    print("\n================Menu=================")
    print('1:Reserve ticket:')
    print('2:Show Reserved Trains:')
    print('3.Exit:')

    ch = int(input("Enter Your Choice:"))
    if(ch==1):
    	train = input("Please Enter Train No And Name: ")
    	date = input("Please Enter Date of Journey: ")
    	train_class = input("Please Enter class(First or Second:)")
    	seat = int(input("Please Enter no of Berths/seats:"))
    	starting_From=input("Please Enter Station Name where to Start:")
    	destination = input("Enter destination Name:")
    	Rail.reservation(train,date,train_class,starting_From,destination)
    elif(ch == 2):
    	Rail.showtrains()
    elif(ch == 3):
    	sys.exit(0)
    else:
    	print("Please Enter Valid Choice")