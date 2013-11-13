def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, ew can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)	

def adrian_avgfunction(grades):
	''' (array)->num
	function returns average of grades.
	adrian_function([2,3,4])>>> 3'''
	sum_grades = 0
	for i in grades:
		sum_grades += i
	sum_grades/len(grades)
	print sum_grades/len(grades)
	
adrian_avgfunction([23,940,234])
adrian_avgfunction([56.39,99])
adrian_avgfunction([23+32,423,44])
adrian_avgfunction([1,2,3])

	