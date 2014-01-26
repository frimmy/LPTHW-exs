from sys import exit
import random
import time
import math

def greenpath(player):
	'''string-> none'''
	print "\n%s is led to the forest habitat." % player.name
	print "%s hears the sounds of a bamboo-munching pack of pandas." % player.name
	print "Although heard, they cannot be seen..."
	print "A door can be seen just beyond the tree line"
	
	if player.keys != []:
		print "\nYou've got the key!"
		next = raw_input("Enter 'back' to go back to the room you started.\nEnter 'blue' to visit the fairy.\n:> ") 
		
	else:
		print"\nMake a break for it? Crawl silently along the forest floor? Make balloon animals?"
		next = raw_input("Enter 'run' to run, 'crawl' to crawl, or 'blow' to make balloon animals\n>: ")
		
		if next == "run":
			die("\n%s runs left.. %s runs right.. \nBut %s doesn't run faster than a pack of startled pandas." % (player.name,player.name,player.name),player)
		elif next == "crawl":
			die("\n%s crawls ever so slowly..but pandas aren't deaf"%player.name,player)
		elif next == "blow":
			print "\nEveryone knows that hungry pandas love bamboo." 
			print "Who'd have thought hungry pandas also go panda-shit for balloon animals?"
			blue_key_room(player)
		else:
			next += "?! That doesn't even make sense!"
			die(next,player)
	
		
	if next == "back":
			start(player)
	elif next == "blue":
			blue_key_room(player)
	else:	
		die("Failing in understanding directions is failing at life..",player)
		
def blue_key_room(player):
	print "\nWelcome to the blue key room, %s!" %player.name
	
	if "blue key" not in player.keys:
		print "The blue key fairy gives you the blue key!"
		player.keys.append("blue key")
		print "Your keys: ",player.keys
		print "And the blue key fairy bids you farewell.."
		raw_input("Press return to return back to the green path..")
		greenpath(player)
	else:
		print "You've already been given the blue key!"
		print "And the blue key fairy bids you farewell.."	
		raw_input("Press return to return back to the green path..")
		greenpath(player)
		
def yellowpath(player):
	'''string, array -> none'''
	print "\nThe yellow path is long and lined in gold."
	time.sleep(1)
	print "At the end of the path is a blue door.."
	
	if 'boss key' in player.keys:
		print "The golden monkeys jump up and down.."
		print "You already have the boss key, get outta here!"
		raw_input("Press return to return to the cave.")
		start(player)
	else:
		pass
		
	print "%s tries to open it.." % player.name
	time.sleep(1)
	
	if 'blue key' not in player.keys:
		print "\n%s find that the door is locked." % player.name
		raw_input("Press return to go back to the cave")
		start(player)
	else:
		print "\n%s opens the door with the blue key"% player.name
	
	print "\nThe room is golden, golden floor, golden trees.."
	print "%s sees that even the trees have gold fruit!" % player.name
	print "But the Math-monkeys won't let %s continue without playing their game" % player.name
		
	print "\nA golden monkey asks what breakfast was eaten this morning..."
	question1 = raw_input(">: ")
		
	print "\"%s\", a second Golden Monkey splutters aloud. \"THAT'S GROSS!\"" % question1
	print "The third Golden Monkey asks what the capital of Australia is.." 
	question2 = raw_input(">: ")
	print "%s? We'll buy that.. " % question2
	
	time.sleep(1.2)
	print "\nYou'll have exactly 5 seconds to answer the next question \nto receive the golden key..."
	time.sleep(1.5)
	print "Ready?"
	for i in range(-3,0):
		print abs(i)
		time.sleep(1)
	a,b = random.randint(6,12), random.randint(6,12)
	answer = a*b
	print "What is %d times %d?!" % (a,b)
	quest_start = time.time()
	player_answer = raw_input(">: ")
	quest_end = time.time()
	
	if quest_end - quest_start > 5:
		die("Golden Monkeys don't have that kind of patience..",player)
	elif not player_answer.isdigit():
		print player_answer,"?!"
		die("That, my friend, is not a number. You're beaten to death by the Math Monkeys!",player)
	elif int(player_answer) != answer:
		die("Good guess! Butcha guessed wrong. You're smashed to a pulp by countless Golden Math Monkeys!",player)
	else:
		print "...what..."
		time.sleep(2)
		print "You solved our riddle! Take the boss key!"
		player.keys.append("boss key")
		print "Your keys: ",player.keys
		print "Good luck on your journey %s" % player.name
		raw_input("Press return to return back to the cave..")
		start(player)
	
def smaug_attack(player,player_hp):
	damage = math.floor(3*random.random())+1
	smaug_miss = math.floor(4*random.random())
	if smaug_miss == 0:
		print "Smaug missed!"
	else:
		print "Smaug slashes %s" % player.name
		print "%s loses %d HP!" % (player.name,damage)
	return player_hp - damage
		
def player_attack(player, smaug_hp, swing):
	if swing == 's':
		print "%s swings at Smaug with the Sword of Valor!" % player.name
		player_miss = math.floor(5*random.random())
		crit_hit = 0
		damage = 3
		
	elif swing == 'p':
		player_miss = math.floor(5*random.random())
		crit_hit = math.floor(3*random.random())
		damage = 1
		print "%s swings at Smaug with ..." % player.name
		time.sleep(1)
		print "...fists?!"
	else:
		print "SMAUG CACKLES at your stupidity...typing errors are for FOOLS."
		return smaug_hp
		
	
	if player_miss == 0:
		print "%s missed!" % player.name
		damage = 0
	elif crit_hit != 2:
		print "%s clobbers Smaug" % player.name
		print "Smaug loses %d HP!" % damage
	else:
		print "CRITICAL HIT! %s punched Smaug in his spleen!" % player.name
		damage = 5
	
	return smaug_hp - damage
	
def boss_door(player):
	# print "this will be the Boss code"
	smaug_life = 25 #declared Smaug HP and player HP
	player_life = 15
	
	if 'boss key' not in player.keys:
		print "\n%s finds that the door is locked.." % player.keys
		raw_input("Press return to go back to the cave")
		start(player)
	else:
		time.sleep(1)
		print "\n%s opens the door with the Boss key!"% player.name
		
	print "The dragon, Smaug, greets you with flames!"
	print "He sits atop a pile of gold estimated to be worth..."
	time.sleep(1)
	print "$1.2 TRILLION Net Present Value!..."
	time.sleep(1)
	print "But he's just going to give it to you.."
	
	print "\nQuickly, pick up the Sword of Valor!"
	print "You have 3 seconds, type 'sword'!"
	sword_start = time.clock()
	next = raw_input(">: ")
	sword_end = time.clock()
			
	if sword_end - sword_start > 3:
		die("Too slow! You're ROASTED.",player)
	elif next != "sword":
		print "%s?!" % next
		die("You need a sword to defeat Smaug. ROASTED.",player)
	else: 
		print "The Sword of Valor is yours!"
	
	while smaug_life > 0:
		if player_life < 1:
			print "Mmmm, Smaug loves barbecued %s for dinner" % player.name
			print "%s ran out of HP!..." % player.name
			die("You're toast!",player)
		else:
			print "\n%s has %d HP remaining" % (player.name, player_life)
			print "Smaug has %d HP remaining." % smaug_life
			
			print "Type 's' to swing your sword for 2 damage."
			print "Type 'p' to punch for 1 damage with 1/3 chance of critical hit for 5 damage.."
			next = raw_input(">: ")
		
			print "Smaug takes a swing at %s" % player.name
			player_life = smaug_attack(player, player_life)
			smaug_life = player_attack(player,smaug_life,next)
			
	
	end()


def start(player):
	print "******************************"	
	print "\n%s is in a dark dimly lit cave" % player.name	
	print "To %s's left, there is a green path and a yellow path." % player.name
	print "To %s's right, a locked door." % player.name
	print"Pick a path or open the door to continue." 
	
	next = raw_input("\nEnter choice to proceed \n'green' for green path \n'yellow' for yellow path \n'door' for the Boss door\n>: ").lower()
	
	if next =='green':
		greenpath(player)
		#passes player object with lives, keys, name
		
	elif next == 'yellow':
		yellowpath(player)
		#passes player object with lives, keys, name
	elif next == 'door':
		boss_door(player)
		#passes player object with lives, keys, name
	else:
		print "xxxxxxxxxxxxxxxxxxxxxxxx\n"
		die(next+" ?! %s chokes on phlegm and drowns to death." % player.name,player)
		#passes player object with lives, keys, name

def die(reason,player):
	player.lives-=1
	
	if player.lives > 0:
		print reason,"?! You're dead. :-( Play again?"
		raw_input("press return to continue")
		print "\n******************************"
		if player.lives > 1:
			print "%s has %d lives." % (player.name, player.lives)
		else:
			print "%s has %d life..." % (player.name, player.lives)
		start(player)
	else:
		print reason,"?! You're dead, D-E-A-D. DEAD!!!"
		print "Congrats'n thanks for playing\n..."
		exit(0)
def end():
	print "Smaug is slain! You win the gold!"
	print "**********************************"
	print "Thanks for playing"
	print "Credits"
	time.sleep(1)
	print "Written by, created, designed, developed by..."
	time.sleep(1)
	print "Adrian Frimpong" 
	exit(0)
print "\nWelcome to MINES OF PYTHAGORA..."
print "********************************"
print "\n"


class Player(object):
	"""docstring for Player"""
	def __init__(self):
		
		self.name = raw_input(">: Enter your name")
		self.keys = []
		self.lives = 3
		
raw_input("press return key to continue\n")
newPlayer = Player()

gamekeys = newPlayer.keys
player = newPlayer.name

print "%s has %d lives." % (player,newPlayer.lives)

start(newPlayer)


