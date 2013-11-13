from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take? Enter a number"
	
	next = raw_input("> ")
	
	if next.isdigit():
		how_much = int(next)
	else: dead("Man, learn to type a number!")
		
	if how_much < 50:
		print "Nice, you're not greedy! You win."
		exit(0)
	else:
		dead("You greedy bastard!")
		
def ball_pit_room():
	print "\nIn front of you, an expanse of plastic balls like never seen before...\n"			
	print "Above, the Griffin circles awaiting your next move."
	print "Fortunately, you're equipped with your sharp mind, and on the floor \nlays an even sharper sword.."
	print " You could return from WHENCE YOU CAME...or...\n"
	
	
	next = raw_input("\nEnter 'pick up' to pick up the sword, 'dive in' to jump into the ball pit,\n or 'turn around'\n\n> ").lower()
	
	griffin_hit = 0
	
	if next == "pick up":
		print "\nAh, brave soul, care to take a swing at the Beast?!"
		next = raw_input("\nEnter 'take swing' to swing your sword or 'turn around' to leave.\n>   ")
	elif next == "dive in":
		dead("\nA tad early for a dip with a Griffin overhead. EYES RAKED.") 
	elif next == "turn around":
		dead("\nWhere are you going?...think the Griffin is just going to let you off Scott free?")
	else:
		dead(next+"\n What's that even mean?")
	
	
	while griffin_hit < 2:
		if next == "take swing":
			griffin_hit += 1
			if griffin_hit <2:
				print "\nHyah. HYEAH! The griffin has been hit once!"
			else:
				print "\nHyah. HYEAH! The griffin has been hit %d times!" % griffin_hit
				
			if griffin_hit <2:
				next = raw_input("\nEnter 'take swing' to swing your sword or 'turn around' to leave.")
			else:
				print "\nHARK, THE GRIFFIN IS DEAD!"
		elif next == "turn around":
			dead("\nTurn around with the GRIFFIN ALIVE?! Tis a shame to die to a Griffin with a sword in hand...")
		else:
			dead(next)
			
	print "\nWith the Griffin slain, you are free to do as you please! Also a NEW door appears.."
	next = raw_input("\nEnter 'turn around' to go back from whence you came, \n'open new door' to continue to a new room, or 'dive in' to suit your ball pit fancies.").lower()
	
	if next == "turn around":
		start()
	elif next == "open new door":
		gold_room()
	elif next == "dive in":
		dead("\nBall pits foreverrrrr")
	else:
		dead("\nhmm...interesting choice, GAME OVAH")
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		if not bear_moved:
			next = raw_input("Enter 'take honey' or 'taunt bear'\n> ").lower()
		else:
			next = raw_input("Enter 'take honey' or 'taunt bear' or 'open door'\n> ").lower()
			
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now by entering"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

def cthulhu_room():
	print "\nHere you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("Enter 'flee' or 'eat your head'\n> ").lower()
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	end  = raw_input('Press return key to exit')
	# print end
	exit(0)
	
def start():
	print "\nYou are in a dark room."
	print "There is a door to your right, a door to your left, and one marked 'ball pit'."
	print "Which one do you take?\n"
	
	next = raw_input("Enter 'left','right', or 'ball pit'\n> ").lower()
	
	if next == "left": 
		bear_room()
	elif next == "right":
		cthulhu_room()
	elif next == "ball pit":
		ball_pit_room()
	else:
		dead("Ha. You stumble around the room until you starve.")
		
start()