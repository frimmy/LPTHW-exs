the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
#Same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also we can go through mixed lists tool
#notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i
	
#we can also build lists, first start with an empty one
elements = []
elements = range(0,6)
#then use the range function to do 0 to 5 counts
for i in elements:
	print "This is in the elements list: %d" % i
	# append is a function that lists understand

	
#now we can print them out too


L = list(range(0,6))
for i in L:
	print "This is in L: %d" % i	