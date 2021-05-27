# Write a python program to create a thread and use it to run a function.
from threading import Thread 
from time import sleep 

# function to create threads 
def threaded_function(arg): 
	for i in range(arg): 
		print("Running") 

# wait 3 sec in between each thread 
sleep(3) 


if __name__ == "__main__": 
	thread = Thread(target = threaded_function, args = (5, )) 
	thread.start()
	thread.join()
	print("thread finished...exiting")	
