sqSum = 0
sumSq = []
for i in xrange(1,101):
	sumSq.append(i*i)
	sqSum += i

print sqSum**2 - sum(sumSq)
