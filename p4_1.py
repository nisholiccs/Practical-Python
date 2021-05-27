
import time
import threading
from threading import Thread

def sleepMe(i):
	print("Thread %s going to sleep for 5 seconds." % threading.current_thread())
	time.sleep(5)
	print("Thread %s is awake now.\n" % threading.current_thread())

#Creating only four threads for now
for i in range(4):
	th = Thread(target=sleepMe, args=(i, ))
	th.start()
