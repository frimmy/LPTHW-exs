# def is_palin(num):
# 	return str(num) == str(num)[::-1]

# print is_palin("nun")

# maxpal = 0
# for a in range(999,99,-1):
# 	for b in range(a,99,-1):
# 		if is_palin(a*b) and a*b > maxpal:
# 			maxpal = a * b

# print maxpal

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def smallest_div_twenty(step):
	for num in xrange(step,999999999, step):
		if all(num % n == 0 for n in check_list):
			return num
	return None
if __name__ == '__main__':
	solution = smallest_div_twenty(2520)
	if solution is None:
		print "NO answer found"
	else:
		print "found an answer: ", solution


# 	allCan = 8
# 	canIt = 0
# 	for i in :
# 		if num%i == 0:
# 			canIt += 1
# 			# print "got one"
# 	return canIt == allCan

# minDiv = 2432902008176640000
# print smallest_div_twenty(2432902008176640000)
# # x = 1
# # while not(smallest_div_twenty(x)):
# # 	if (smallest_div_twenty(x)) and x < minDiv:
# # 		minDiv = x
# # 		print "iterated ", x, " times" 
# # 	x+=1	

# # print minDiv

