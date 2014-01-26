def reverse_str(str):
	'''(str)--> str
	reverses str object
	reverse_str('apple')>>> 'elppa'
	reverse_str('bear')>>> 'reab'
	reverse_str('adrian')>>> 'nairda
	reverse_str('carrac')>>> 'carrac'
	reverse_str('')>>> '' 
	'''
	reversed_str = ''
	for x in xrange(-1,-len(str)-1,-1):
		reversed_str+= str[x]
	return reversed_str

print reverse_str('apple')

def is_palindrome(str):
	'''(str)-->bool
	is_palindrome('car')--> false
	is_palindrome('racecar')--> true
	is_palindrome(234)--> 'wtf that ain't a number'
	'''
	return str == reverse_str(str)

print is_palindrome('car')
print is_palindrome('racecar')
# is_palindrome(234)

def is_unique(string):
	'''(str)---> bool

	returns whether all characters in a string are unique.

	is_unique('race')---> true
	is_unique('racecar') ---> false
	is_unique(234) ---> 'wtf that ain't a string

	'''
	# countDoubles = True
	
	strchar = set()
	for i in xrange(0,len(string)):
		if string[i] not in strchar:
			strchar.add(string[i])
		else:
			return False 
			# print strchar
	return True

print is_unique('race')
print is_unique('racecar')
print is_unique('adrian')
print is_unique('beavis')