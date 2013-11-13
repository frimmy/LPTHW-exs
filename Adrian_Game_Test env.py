import time as t
import msvcrt



osys = raw_input("Press w for windows,l for linux ")
if (osys == "w"):
    pass
else:
    pass 
### windows version...
def raw_input_with_timeout_ms(prompt, timeout=05.0):
	print prompt
	finishat = t.time() + timeout
	result = []
	while True:
		if msvcrt.kbhit():
			result.append(msvcrt.getche())
			if result[-1] == '\r':   # or \n, whatever Win returns;-)
				return ''.join(result)
			t.sleep(0.1)          # just to yield to other processes/threads
		else:
			if t.time() > finishat:
				return "out of time!"
# Test for Windows raw input with time out
a = raw_input_with_timeout_ms("How old are you?")

if a == "out of time!":
	print a
elif int(a) <= 20:
	print "Huh..you're young."
elif int(a) > 20:
	print "Wow, you're old"
else:
	print "well that doesn't make sense"
