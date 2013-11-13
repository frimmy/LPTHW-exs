from sys import argv

script, user_name, user_ht = argv
what_say = '> '

print "Hi %s of %s, I'm the %s script." % (user_name, user_ht, script)
print " I'd like to ask you a few questions."
print "Do you like me %s of %s?" % (user_name, user_ht)
likes = raw_input(what_say)

print "Where do you live %s" % user_name 
lives = raw_input(what_say)

print "What kind of computer do you have? And do they have them in %s" % user_ht
computer = raw_input(what_say)

print """
Alright, so you said %r about liking me.
You lives in %r. Not sure where that is..
And you have a %r computer. Nice. Have fun in the %s
""" % (likes, lives, computer, user_ht)