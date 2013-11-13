#variable for string using %d as formatted variable
x = "There are %d types of people." % 10

#string variables binary and do_not declared
binary = "binary" 
do_not = "don't"

#variables used to combine 
y = "Those who know %s and those who %s." % (binary, do_not)

#prints variables x and y
print x
print y

#prints the variables as formatted variables
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#prints joke_evaluation using nested formatted variable to link to 'hilarious' variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

#concatenates 'w' and 'e' and prints both string variables
print w + e
