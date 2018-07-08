from sys import argv

script, user_name, bb = argv
prompt = '>'

print "Hi %s I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you lives %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do yu have?"
computer = raw_input (prompt)

print """
Alrihat, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

print "Hi %s." % bb
print "Do you like me %s?" % bb
likes_bb = raw_input(prompt)
print "So, you said %r about liking me." % likes_bb
