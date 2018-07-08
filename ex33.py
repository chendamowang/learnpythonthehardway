numbers = []

def f(a, b):
    i = 0
    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += b
        print "Numbers now: ", numbers
        print "At the bottom i is", i

a = int(raw_input("a is?"))
b = int(raw_input("b is?"))
f(a,b)

for number in numbers:
    print number
