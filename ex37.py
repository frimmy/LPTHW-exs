#######
#1. Write Out keywords from memory
#2. If wrong, write down on a card
#3. if didn't know, write down aand save for frther research later
#4. Finally, incorporate each into a small Python program 
#	or as many as can be made.


# Data Types
# True, False, None
# strings = {a:'a',b:'b',c:'c'}
# numbers = [1,2,3,4,4...]
# floats = [2.2,234.3,234.0...]
# lists = [strings,floats]

# String Escape Sequences
# print "\\ \' \" \a \b \f \n \r \t \v"
# print "%d , %i ,%o, %u %x %X %e %E %f %F %g %G %c %r %s %%" 

# Operators
# @?
# <>?
# []?
# {}?
# ;?

# ---------------------------------------------------------------------
# import: import modules, methods from modules, etc
# as: duhh i know this one, alias for imported modules/classes/files etc.
# print: prints a statement to the console
# and: conditional to join two conditions
# from: used in import statements to pull specific functions from defined modules

import time as t
print "What's your name?"
a = raw_input(">: ")
t.sleep(1)
# ----------------------------------------------------------------------
# elif: additional conditional in if statements
# or: keyword to join two conditionals that passes if either condition is True
# else: if a series of conditions do not pass, then the statements in the else clause are executed
# if: first condition that if true, a series of statements are executed
# pass: does just that, continues on to other statements, allows code to continue executing

#-----------------------------------------------------------------------
# try: first part of try/catch statements, will run through a series of statements until an error occurs

# except: on specified errors, statements under a specific clause 
try:
	if a == 3 and a >= 0:
		print "you understand the and condition"
	elif a is 'Adrian':
			print "That is indeed your name" 
	elif int(a) > 4:
		print "This sure is a high numba" 
	else:
		print "nah!"
except ValueError:
	print "Whoopsies, you didn't enter an integer, but at least"
	print "I've gotta grasp on try/except clauses..."

print a
# def: keyword in defining functions
def function():
# global: refers to variables, specifies that a variable used ... i don't fugign know..
	global a
	a = "changed onna mutha fugga"
	print a
	t.sleep(1)
function()
# with: will close an object with the __init__ and inherited __finally__. if no __finally__, error is raised
with open('output.txt','w') as f:
	a = "den we changed it on dem agin."
	f.write(a)
	
print a

#----------------------- return: returns a value/object as result of a function---------------------#
list1 = []
for j in [1,2,3,4,'cat']:
	print j
	list1.append(j)
	
def function2(list):
	print list
	list.append(3**3)
	return list
	
del list1[4]
print list1
list2 = function2(list1)
print list2

# -------------------------Assert-----------------------------------------------#
# assert: raises user defined errors! helpful for debugging..
while len(list2) < 10:
	list2.append('birds')

print list2	

try:
	assert len(list2) < 8 
except AssertionError:
	print "Damn, it look like we understand assert statements too.."
	list2.pop()
else:
	print "guess no errors generated.."
finally:#----after all the shit, whether or not errors generate, run the finally block----------#
	# ---------------finally--------#
	print "and at the end of it all, we still got it going on.."
print list2

#--------------------------------yield-----------------------------------#
# used to return results from a generator object (similar to a list, but doesn't store values;
# instances are created, and then deleted from memory


def createGenerator():
	for i in range(3):
		yield i*i
mygen = createGenerator()
for i in mygen:
	print i
	
for i in mygen:
	print i


# break: totally wrong, these are used to break out of loops(for or while), similar to Exit For in VBA
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
#the code below will exit the endless for loop when 22 is called by the random integer generator
			break
	else:
		print n, 'is a prime number'

#user exceptions can be raised via the raise keyword
#also, 2 birds 1 stone, we're MAKIN a class.

class YesNoException(Exception):
	def __init__(self):
		print "Invalid value"

print "\nTesting the class we created and the user-defined raise keyword"
print "Enter 'y' or 'no' to the whether you've been to Africa in the past 7 years"

try:
	answer = raw_input(">: ")

	if answer != 'yes' and answer != 'no':
		raise YesNoException
	else:
		print "Correct Value, thanks!" 
except YesNoException:
	print "Gotta enter 'yes' or 'no' dummy.." 
finally:
	print "see, we starting to grasp these basics, schon.."
# class: holds multiple functions, used in object oriented programming...buuut i really ain't too sure yet
# from online Python tutorial...

class Complex:
	def __init__(self,realpart, imagpart):
		self.r = realpart
		self.i = imagpart
x = Complex(3.0, -4.5)
print x.r, x.i

#continue is like the Next x in VBA, it continues to the next item in the loop without running the block underneath..pretty neat!

for i in [x for x in range(0,8)]:
	if i%3 == 0:
		# print i," is chill"
		continue
	print i	


# exec: dynamically runs python code?
exec("for i in [1,2,3,4,5]: print i,")

# is:...? i believe this tests whether an object = typeOf object

print None is None
print True is True
print [] is []
print [] == []

#lambda creates anonymous functions, so you don't have to define the function...cool
for i in (1,2,3,4,5):	
	a = lambda x: x*x
	print a(i),
	
print "\\this is a backslash \n this is an apostrophe\'\n this is a quote\""
print "don't know what this is...perhaps it adds?\a but what?!"
print "or this\b "
print "or this\f "
print "newline\nsee?",
print "return carriage? \r see?"
print "tab\tsee?"
print "donnoez\v"  
