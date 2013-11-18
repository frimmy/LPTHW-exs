class Parent(object):
	"""docstring for Parent"""
	def implicit(self):
		print "PARENT implicit()"
	
	def __init__(self,name):
		self.name = name

	def override(self):
		print "Parent override()"
	
	def scream(self):
		print "AGHH MY NAME IS " + self.name



class Child(Parent):
	def override(self):
		print "Child override()"

dad = Parent('Adrian')
son = Child('Oscar')

dad.scream()
son.override()

		