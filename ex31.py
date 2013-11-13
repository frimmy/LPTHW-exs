print "You enter a dark room with four doors. \n	Do you go through door #1, door #2, door #3, or door#4?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear...ATE your FACE OFF. God job!"
	elif bear == "2":
		print "The bear ...EATS UR LEGS OFF. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
	print "You stare into the endless abyss at Cthulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
	print "Is this a dagger I see before me?" 
	print "1. Grab the dagger" 
	print "2. Call the popos. Knives are dangerous"
	print "3. Do you boo. Do you"
	
	knife = raw_input("> ")
	
	if knife == "1":
		print "Quickly turning around, you knifed HAMLET! Good job!"
	elif knife == "2":
		print "Ha. Like you'd think of bringing a phone to the room full of doors. Hamlet stabs you in BOTH kidneys. Good job!"
	elif knife == "3":
		print "Never a finer time to do the hokey pokey. Shuffled your way into Hamlet'a knife!"
	else:
		print "haha wow... so %s is your idea of dealing with daggers? HAMLET'S KNIVE FOREVER IN YOUR BOOTY. %s ..." % (knife,knife)
elif door == "4":
	print "Magic door number four, who in here deserves more?"
	print "1. Me?"
	print "2. You?"
	print "3. ...NO ONE."
	
	more = raw_input("> ")
	
	if more == "3":
		print "No one hmm? Your spite has paid off! Lavish riches for you and your progeny!"
	else:
		print "THIS IS BIGGER THAN EITHER OF US KNOWS. NO PIE FOR YOU. NO PIE FOR ME. NO PIE FOR ANYONE"
		
	
else:
	print "You stumble around and fall on a knife and die. Good job!"
