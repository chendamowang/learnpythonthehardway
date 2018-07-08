name = 'Zed A. Shaw'
age = 35
height = 74 *2.54 # inches
weight = 180 *0.45359 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name 
print "He's %r cm tall." % height
print "He's %r kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s dependind on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, weight, height, age + height + weight) 
