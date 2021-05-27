# Write a python program where two threads are acting on the same method to 
# allot a berth for the passenger.
import threading 

def print_cube(num): 
	# function to print cube of given num
	print("Cube: {}".format(num * num * num)) 

def print_square(num): 
	# function to print square of given num
	print("Square: {}".format(num * num)) 

if __name__ == "__main__": 
	t1 = threading.Thread(target=print_square, args=(15,)) 
	t2 = threading.Thread(target=print_cube, args=(5,)) 

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done!")
