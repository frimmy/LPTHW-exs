
numbers = []

def throwNum(x,y):
	i = 0
	while i < x:
		print "At the top i is %d" % i 
		numbers.append(i)
		
		i+=y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
num2 = [] 
def throwNum2(x):
	for i in range(0,x):
		print "At the top i is %d" % i
		num2.append(i)
		i+=2
		print i
		print "Num2 now ", num2
		print "At the bottom, i is %d" % i
throwNum(int(raw_input("> range max: ")),int(raw_input("> increase by?")))
for num in numbers:
	print num
	
throwNum2(int(raw_input("> range max: ")))

for numz in num2:
	print numz
