from sys import exit
import random
import time
import math

def greenpath(lives,keys):
	'''string-> none'''
	print "\n%s is led to the forest habitat." % player
	print "%s hears the sounds of a bamboo-munching pack of pandas." % player
	print "Although heard, they cannot be seen..."
	print "A door can be seen just beyond the tree line"
	
	if keys != []:
		print "\nYou've got the key!"
		next = raw_input("Enter 'back' to go back to the room you started.\nEnter 'blue' to visit the fairy.\n:> ") 
		
	else:
		print"\nMake a break for it? Crawl silently along the forest floor? Make balloon animals?"
		next = raw_input("Enter 'run' to run, 'crawl' to crawl, or 'blow' to make balloon animals\n>: ")
		
		if next == "run":
			die("\n%s runs left.. %s runs right.. \nBut %s doesn't run faster than a pack of startled pandas." % (player,player,player),lives,keys)
		elif next == "crawl":
			die("\n%s crawls ever so slowly..but pandas aren't deaf"%player,lives,keys)
		elif next == "blow":
			print "\nEveryone knows that hungry pandas love bamboo." 
			print "Who'd have thought hungry pandas also go panda-shit for balloon animals?"
			blue_key_room(lives,keys)
		else:
			next += "?! That doesn't even make sense!"
			die(next,lives,keys)
	
		
	if next == "back":
			start(lives,keys)
	elif next == "blue":
			blue_key_room(lives,keys)
	else:	
		die("Failing in understanding directions is failing at life..",lives,keys)
		
def blue_key_room(lives,keys):
	print "\nWelcome to the blue key room, %s!" %player
	
	if "blue key" not in keys:
		print "The blue key fairy gives you the blue key!"
		keys.append("blue key")
		print "Your keys: ",keys
		print "And the blue key fairy bids you farewell.."
		raw_input("Press return to return back to the green path..")
		greenpath(lives,keys)
	else:
		print "You've already been given the blue key!"
		print "And the blue key fairy bids you farewell.."	
		raw_input("Press return to return back to the green path..")
		greenpath(lives,keys)
		
def yellowpath(lives,keys):
	'''string, array -> none'''
	print "\nThe yellow path is long and lined in gold."
	time.sleep(1)
	print "At the end of the path is a blue door.."
	
	if 'boss key' in keys:
		print "The golden monkeys jump up and down.."
		print "You already have the boss key, get outta here!"
		raw_input("Press return to return to the cave.")
		start(lives,keys)
	else:
		pass
		
	print "%s tries to open it.." % player
	time.sleep(1)
	
	if 'blue key' not in keys:
		print "\n%s find that the door is locked." % player
		raw_input("Press return to go back to the cave")
		start(lives,keys)
	else:
		print "\n%s opens the door with the blue key"% player
	
	print "\nThe room is golden, golden floor, golden trees.."
	print "%s sees that even the trees have gold fruit!" % player
	print "But the Math-monkeys won't let %s continue without playing their game" % player
	
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
		die("Golden Monkeys don't have that kind of patience..",lives,keys)
	elif not player_answer.isdigit():
		print player_answer,"?!"
		die("That, my friend, is not a number. You're beaten to death by the Math Monkeys!",lives,keys)
	elif int(player_answer) != answer:
		die("Good guess! Butcha guessed wrong. You're smashed to a pulp by countless Golden Math Monkeys!",lives,keys)
	else:
		print "...what..."
		time.sleep(2)
		print "You solved our riddle! Take the boss key!"
		keys.append("boss key")
		print "Your keys: ",keys
		print "Good luck on your journey %s" % player
		raw_input("Press return to return back to the cave..")
		start(lives,keys)
	
def smaug_attack(name,player_hp):
	damage = math.floor(3*random.random())+1
	smaug_miss = math.floor(4*random.random())
	if smaug_miss == 0:
		print "Smaug missed!"
	else:
		print "Smaug slashes %s" % name
		print "%s loses %d HP!" % (name,damage)
	return player_hp - damage
		
def player_attack(name, smaug_hp, swing):
	if swing == 's':
		print "%s swings at Smaug with the Sword of Valor!" % player
		player_miss = math.floor(5*random.random())
		crit_hit = 0
		damage = 3
		
	elif swing == 'p':
		player_miss = math.floor(5*random.random())
		crit_hit = math.floor(3*random.random())
		damage = 1
		print "%s swings at Smaug with ..." % player
		time.sleep(1)
		print "...fists?!"
	else:
		print "SMAUG CACKLES at your stupidity...typing errors are for FOOLS."
		return smaug_hp
		
	
	if player_miss == 0:
		print "%s missed!" % player
		damage = 0
	elif crit_hit != 2:
		print "%s clobbers Smaug" % player
		print "Smaug loses %d HP!" % damage
	else:
		print "CRITICAL HIT! %s punched Smaug in his spleen!" % player
		damage = 5
	
	return smaug_hp - damage
	
def boss_door(lives,keys):
	# print "this will be the Boss code"
	smaug_life = 25 #declared Smaug HP and player HP
	player_life = 15
	
	if 'boss key' not in keys:
		print "\n%s finds that the door is locked.." % player
		raw_input("Press return to go back to the cave")
		start(lives,keys)
	else:
		time.sleep(1)
		print "\n%s opens the door with the Boss key!"% player
		
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
		die("Too slow! You're ROASTED.",lives,keys)
	elif next != "sword":
		print "%s?!" % next
		die("You need a sword to defeat Smaug. ROASTED.",lives,keys)
	else: 
		print "The Sword of Valor is yours!"
	
	while smaug_life > 0:
		if player_life < 1:
			print "Mmmm, Smaug loves barbecued %s for dinner" % player
			print "%s ran out of HP!..." % player
			die("You're toast!",lives,keys)
		else:
			print "\n%s has %d HP remaining" % (player, player_life)
			print "Smaug has %d HP remaining." % smaug_life
			
			print "Type 's' to swing your sword for 2 damage."
			print "Type 'p' to punch for 1 damage with 1/3 chance of critical hit for 5 damage.."
			next = raw_input(">: ")
		
			print "Smaug takes a swing at %s" % player
			player_life = smaug_attack(player, player_life)
			smaug_life = player_attack(player,smaug_life,next)
			
	
	end()


def start(lives,keys):
	print "******************************"	
	print "\n%s is in a dark dimly lit cave" % player	
	print "To %s's left, there is a green path and a yellow path." % player
	print "To %s's right, a locked door." % player
	print"Pick a path or open the door to continue." 
	
	next = raw_input("\nEnter choice to proceed \n'green' for green path \n'yellow' for yellow path \n'door' for the Boss door\n>: ").lower()
	
	if next =='green':
		greenpath(lives,keys)
		
	elif next == 'yellow':
		yellowpath(lives,keys)
		
	elif next == 'door':
		boss_door(lives,keys)
	else:
		print "xxxxxxxxxxxxxxxxxxxxxxxx\n"
		die(next+" ?! %s chokes on phlegm and drowns to death." % player,lives,keys)
		

def die(reason,lives,keys):
	lives-=1
	
	if lives > 0:
		print reason,"?! You're dead. :-( Play again?"
		raw_input("press return to continue")
		print "\n******************************"
		if lives > 1:
			print "%s has %d lives." % (player,lives)
		else:
			print "%s has %d life..." % (player,lives)
		start(lives,keys)
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

raw_input("press return key to continue\n")
player = raw_input("Enter player name:> ")

gamekeys = []
startlives = 3
print "%s has %d lives." % (player,startlives)

start(startlives,gamekeys)


