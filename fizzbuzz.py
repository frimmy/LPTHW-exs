fizzbuzzlist = [x for x in range(100)]
# print fizzbuzzlist
for i in fizzbuzzlist:
	if i % 3 == 0 and i % 5 == 0:
		print "FizzBuzz"
	elif i % 3 == 0:
		print "Fizz"
	elif i % 5 == 0:
		print "Buzz"
	else:
		print i
