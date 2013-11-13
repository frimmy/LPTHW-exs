import time as t
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	def __init__ (self):
		print "I'm an animal"
		t.sleep(1)

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		print "Bark bark i'm a dog"
		t.sleep(1)
		print "bark, my name is: ", self.name
		t.sleep(1)	
	def bark(self):
		print "Bark!"

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		print "meow mewo, i'm a cat"
		t.sleep(1)
		print "meow, my name is: ", self.name
		t.sleep(1)
	def meow(self):
		print "Meow!"

## Person is-a object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None
		print "I'm human..and my name is: ",self.name
		t.sleep(1)
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a super class with a name hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		print "I've gotta job making: ", self.salary
		t.sleep(1)
## Fish is-a object
class Fish(object):
	"""docstring for Fish"""
	pass
	def swim(self):
		print "I'm swimming.."
## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	"""docstring for Halibut"""
	pass

## rpver is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet cat named Satan
mary.pet = satan

## frank is-a Employee that has-a salary of 120000
frank = Employee("Frank",120000)

## frank has-a pet dog named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()

print type(harry)

print harry.__class__, frank.name



