name = 'Adrian A Frimpong'
age = 24 #not a lie
height = 71.5 #inches
height_in_cm = int(height*2.254) #height to cm converter
weight = 204 #lbs
weight_in_kilos = int(weight/2.2)

eyes = 'Blue' 
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d cm tall." % height_in_cm
print "He's %d pounds heavy." % weight
print "He's %d kilos heavy." % weight_in_kilos
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "anywhere any time %r is my hair colour" % hair

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	