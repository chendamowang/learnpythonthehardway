# -*- coding:utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the files.  Goodbye!"
target.truncate() # 清空test.txt

print "Now I'm going to ask you for thre lines."

line1 = raw_input("line 1:") # 将用户输入的第一行内容存储在line1
line2 = raw_input("Line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write('%s\n%s\n%s'% (line1, line2, line3))

print "And finally, we close it."
target.close()
