from sys import exit
import random
import time
import math


class Rooms(object):
	'''string, obj -> string 
	the Rooms class provides structure and interactive elements for 
	player to affect and be affected by. Returns the next scene (could be a 
	death scene)
	'''

	def enter(self,player):
		'''takes the player object and interacts with scene affecting the player'''
		print "This scene hasn't been configured yet, Sublcass to implement enter()"
		exit(0)

class Engine(object):
	"""Engine loads up my map for the game as well as 
	the """
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self, player):
		
		current_scene = self.scene_map.open_scene(player)
		
		# print "Play's first scene ", current_scene
		# above statement tested the self.map.scenes
		
		while True:

			print "\n----------------------"
			next_scene_name = current_scene.enter(player)
			#stores the result of the player's scene interaction
			 
			# print "next scene", next_scene_name
			#above statement tested the current_scene.enter function

			current_scene = self.scene_map.next_scene(next_scene_name)
			# loads up the next scene for the player to interact with


class Greenpath(Rooms):
	'''string, obj -> string'''
	def enter(self,player):
		# pass
		player.recent_scene = "greenpath"
		print "\n%s is led to the forest habitat..." % player.name
		print "%s hears the sounds of a bamboo-munching pack of pandas." % player.name
		time.sleep(1.2)
		print "Although heard, they cannot be seen..."
		print "A door can be seen just beyond the tree line"
		
		if player.keys != []:
			print "\nYou've got the key!"
			next = raw_input("Enter 'back' to go back to the room you started.\nEnter 'blue' to visit the fairy.\n:> ") 
			
		else:
			print"\nMake a break for it? Crawl silently along the forest floor? Make balloon animals?"
			next = raw_input("Enter 'run' to run, 'crawl' to crawl, or 'blow' to make balloon animals\n>: ")
			time.sleep(1)
			
			if next == "run":
				player.deathReason = '''\n%s runs left.. %s runs right.. \nBut %s doesn't run faster than a pack of 
				startled pandas.''' % (player.name,player.name,player.name)
				return "die"
			
			elif next == "crawl":
				player.deathReason = "\n%s crawls ever so slowly..but pandas aren't deaf" % player.name
				return "die"

			elif next == "blow":
				print "\nEveryone knows that hungry pandas love bamboo." 
				print "Who'd have thought hungry pandas also go panda-shit for balloon animals?"
				return "blueKeyRoom"
			
			else:
				player.deathReason = "?! That doesn't even make sense!"
				return "die"
		
			
		if next == "back":
				return "start"
		elif next == "blue":
				return "blueKeyRoom"
		else:	
			player.deathReason = "Failing in understanding directions is failing at life.."
			return "die"

class Blue_key_room(object):

	def enter(self, player):
		player.recent_scene = "blueKeyRoom"
		print "\nWelcome to the blue key room, %s!" %player.name
		
		if "blue key" not in player.keys:
			print "The blue key fairy gives you the blue key!"
			player.keys.append("blue key")
			print "Your keys: ",player.keys
			print "And the blue key fairy bids you farewell.."
			raw_input("Press return to return back to the green path..")
			return "greenpath"
		else:
			print "You've already been given the blue key!"
			print "And the blue key fairy bids you farewell.."	
			raw_input("Press return to return back to the green path..")
			return "greenpath"
		
class Yellowpath(object):
	'''string, array -> none'''
	
	def enter(self, player):
		player.recent_scene = "yellowPath"
		print "\nThe yellow path is long and lined in gold."
		time.sleep(1)
		print "At the end of the path is a blue door.."
		
		if 'boss key' in player.keys:
			print "The golden monkeys jump up and down.."
			print "You already have the boss key, get outta here!"
			raw_input("Press return to return to the cave.")
			return "Start"
		else:
			pass
			
		print "%s tries to open it.." % player.name
		time.sleep(1)
		
		if 'blue key' not in player.keys:
			print "\n%s find that the door is locked." % player.name
			raw_input("Press return to go back to the cave")
			return "start"
		
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
			player.deathReason = "Golden Monkeys don't have that kind of patience.."
			return "die"

		elif not player_answer.isdigit():
			print player_answer,"?!"
			player.deathReason = "That, my friend, is not a number. You're beaten to death by the Math Monkeys!"
			return "die"
		
		elif int(player_answer) != answer:
			player.deathReason = "Good guess! Butcha guessed wrong. You're smashed to a pulp by countless Golden Math Monkeys!"
			return "die"
		
		else:
			print "...what..."
			time.sleep(2)
			
			print "You solved our riddle! Take the boss key!"
			player.keys.append("boss key")
			
			print "Your keys: ",player.keys
			print "Good luck on your journey %s" % player.name
			raw_input("Press return to return back to the cave..")
			
			return "start"

class Boss_door(Rooms):
	# print "this will be the Boss code"
	
	def smaug_attack(self, player):
		'''returns new player hp after smaug attacks'''

		damage = math.floor(3*random.random())+1
		smaug_miss = math.floor(4*random.random())
		
		if smaug_miss == 0:
			print "Smaug missed!"
			print "%s doesn't lose any HP!" % player.name
			return player.hp

		else:
			print "Smaug slashes %s" % player.name
			print "%s loses %d HP!" % (player.name, damage)
			
			
		return player.hp - damage
		
	def player_attack(self, player, smaug_hp, swing):
		''' returns smaug's new hp after player attacks'''

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
			
		time.sleep(2)

		if player_miss == 0:
			print "%s missed!" % player.name
			damage = 0
		
		elif crit_hit != 2:
			print "%s clobbers Smaug" % player.name
			print "Smaug loses %d HP!" % damage
		
		else:

			time.sleep(1.5)	
			print "CRITICAL HIT! %s punched Smaug in his spleen!" % player.name
			damage = 5
		
		return smaug_hp - damage


	def enter(self, player):
		player.recent_scene = "boss"
		
		smaug_life = 25
		player.hp = 15
		
		if 'boss key' not in player.keys:
			print "\n%s finds that the door is locked.." % player.name
			raw_input("Press return to go back to the cave")
			return "start"
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
			player.deathReason = "Too slow! You're ROASTED."
			return "die"

		elif next != "sword":
			print "%s?!" % next
			player.deathReason = "You need a sword to defeat Smaug. ROASTED."
			return "die"
		
		else: 
			print "The Sword of Valor is yours!"
		
		while smaug_life > 0:
			if player.hp < 1:
				print "Mmmm, Smaug loves barbecued %s for dinner" % player.name
				print "%s ran out of HP!..." % player.name
				player.deathReason = "You're toast!"
				return "die"
			
			else:
				print "\n%s has %d HP remaining" % (player.name, player.hp)
				print "Smaug has %d HP remaining." % smaug_life
				
				print "Type 's' to swing your sword for 2 damage."
				print "Type 'p' to punch for 1 damage with 1/3 chance of critical hit for 5 damage.."
				next = raw_input(">: ")
				
				time.sleep(1.5)

				print "Smaug takes a swing at %s" % player.name
				player.hp = self.smaug_attack(player)
				smaug_life = self.player_attack(player,smaug_life,next)
				
		
		return "end"

class Start(object):

	def enter(self,player):
		print "******************************"	
		print "\n%s is in a dark dimly lit cave" % player.name	
		print "To %s's left, there is a green path and a yellow path." % player.name
		print "To %s's right, a locked door." % player.name
		print"Pick a path or open the door to continue." 
		
		next = raw_input("\nEnter choice to proceed \n'green' for green path \n'yellow' for yellow path \n'door' for the Boss door\n>: ").lower()
		
		if next =='green':
			return "greenpath"
			#passes player object with lives, keys, name
			
		elif next == 'yellow':
			return "yellowPath"
			#passes player object with lives, keys, name
		elif next == 'door':
			return 'boss'
			#passes player object with lives, keys, name
		else:
			print "xxxxxxxxxxxxxxxxxxxxxxxx\n"
			player.deathReason = next+" ?! %s chokes on phlegm and drowns to death." % player.name
			return "die"
			#passes player object with lives, keys, name


class Die(Rooms):
	
	def enter(self,player):
		player.lives-=1
	
		if player.lives > 0:
			print player.deathReason,"?! You're dead. :-( Play again?"
			raw_input("press return to continue")
			print "\n******************************"
			if player.lives > 1:
				print "%s has %d lives." % (player.name, player.lives)
			else:
				print "%s has %d life..." % (player.name, player.lives)

			print "Continue from last room? Enter 'yes' otherwise enter 'return key' "
			next = raw_input("> ")

			if next == "yes" and player.recent_scene != '':
				return player.recent_scene
			else:
				return "start"
		else:
			print player.deathReason,"?! You're dead, D-E-A-D. DEAD!!!"
			print "Congrats'n thanks for playing\n..."
			exit(0)
class end(Rooms):
	def enter(self,player):
		print "Smaug is slain! %s win the gold!" % player.name
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
		print "Enter your name"
		self.name = raw_input(">: ")
		self.keys = []
		self.lives = 3
		self.deathReason = ''
		self.recent_scene = ''


		


class Map(object):
	"""This class can store the rooms of a game
	It has the ability to import other game maps!
	Use to navigate between rooms. 
	"""
	scenes = {
		"start":Start(),
		"die":Die(),
		"greenpath": Greenpath(),
		"blueKeyRoom":Blue_key_room(),
		"yellowPath":Yellowpath(),
		"boss":Boss_door(),
		"end": end()}

	def __init__(self,start_scene):
		self.start_scene = start_scene
		# sets up map's starting scene
		
	
	def next_scene(self, scene_name):
		'''str->obj returns the next scene for the game'''
		return self.scenes.get(scene_name)
		

	def open_scene(self,player):
		'''gets the start scene defined on creating
		an instance for the map and returns it'''
		return self.next_scene(self.start_scene)

raw_input("press return key to continue\n")
newPlayer = Player()

print "%s has %d lives." % (newPlayer.name,newPlayer.lives)

# TODO move num of players into a separate class
# raw_input("press return key to continue\n")
# newPlayer = Player()
# print "%s has %d lives." % (newPlayer.name,newPlayer.lives)


a_map = Map('start')

a_game = Engine(a_map)

a_game.play(newPlayer)