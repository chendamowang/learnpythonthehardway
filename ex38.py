ten_things = "Aapples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # split(' ', ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff[-1])
    print "Adding: ", next_one
    stuff.append(next_one) # append(stuff, next_one)
    print "There's %d items noe." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) # join(' ', stuff)
print '#'.join(stuff[3:5]) # join('#", stuff[3:5])
