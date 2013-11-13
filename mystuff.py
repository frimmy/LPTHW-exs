#!/usr/bin/python

class Parent:		#defines parent class
	def myMethod(self):
		print "Calling parent method"

class Child(Parent):
	"""docstring for Child"""
	def myMethod(self):
		print "Calling child method"
		
c = Child()		# instance of child
c.myMethod()	# child calls overriden method

# Best Overloading Methods

class ParentTest:
	"""docstring for ParentTest"""
	x=100
	def __init__(self):
		print ParentTest.x
		
		
class ChildTest(Parent):
	"""docstring for ChildTest"""
	def __init__(self):
		print "I'm overriding whatever the fuck i want."

c = ChildTest()
d = ParentTest()
# print c.x
print repr(d)

#!/usr/bin/python

class Vector:
	"""docstring for Vector"""
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return "Vector (%d, %d)" % (self.a, self.b)

	def __add__(self,other):
			return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

#!/usr/bin/python

class JustCounter:
	"""docstring for JustCounter"""
	__secretCount = 0

	def count(self):
		self.__secretCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter._JustCounter__secretCount