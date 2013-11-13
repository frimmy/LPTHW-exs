import time as t
import mystuff as m
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self,song):
		for line in self.lyrics:
			print line
			t.sleep(.33)
			f = open("%s"%song,'a')
			f.write(line)
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
			
understanding = ["Young man, who do you think you are","I said young man, who do you think you are"]
			
ymca = Song(understanding)
happy_bday.sing_me_a_song("cuzin")

bulls_on_parade.sing_me_a_song("cuzin1")

ymca.sing_me_a_song("cuzin2")

a = m.Point()
print a.x
del a

