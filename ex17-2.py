from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how?"

out_file = open(to_file, 'w')
out_file.write(open(from_file).read())
print "Alright, all done."

out_file.close()
