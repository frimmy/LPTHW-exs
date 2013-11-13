import thread 
import threading  
import sys
from select import select

def raw_input_with_timeout(prompt, timeout=5.0):
	timer = threading.Timer(timeout, thread.interrupt_main)
	astring = None
	try:
		timer.start()
		astring = raw_input(prompt)
		
	except KeyboardInterrupt:
		timer.cancel()
		return "Time's up!"
	timer.cancel()
	return astring
print "How old are you?"	
age = raw_input_with_timeout(">: ")
if age > 12:
	print "you're pretty old"
elif age == None:
	print "Why didn't you enter anything?"
else: 
	print "you're pretty young"

# def hello():
	# a = raw_input("testing, enter text: ")
	# return a
	
# t = threading.Timer(3, hello)


# try:
	# t.start()
	# thread.interrupt_main()
# except KeyboardInterrupt:
	# print "error caught"	

