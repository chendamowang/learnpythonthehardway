from sys import argv

script, filename = argv

txt = open(filename)

print "Type the %r." % filename
print txt.read()
