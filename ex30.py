people = 130
cars = 23
buses = 5

if cars > people and people > buses:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if buses > cars or buses < people:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses or people > cars:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."