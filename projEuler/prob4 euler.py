def is_palin(num):
	return str(num) == str(num)[::-1]

print is_palin("nun")

maxpal = 0
for a in range(999,99,-1):
	for b in range(a,99,-1):
		if is_palin(a*b) and a*b > maxpal:
			maxpal = a * b

print maxpal