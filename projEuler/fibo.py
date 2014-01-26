# Fibonacci numbers module 
def __name__():
	return 'fibo'

def fib(n): #write Fibonacci series up to n
	a,b = 0, 1
	result = []
	while b < n:
		a, b = b, a + b
		if b%2==0:
			result.append(b)
		print b,
		
	print "\n\n" + str(sum(result))

def fib2(n): # return Fibonacci series up to n
	result = []
	a, b, x = 0, 1, 0

	while x < n:
		result.append(b)
		a, b = b, a + b
		x+=1
	return result

fib(4000000)