# 
class Animal(object):
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print self.name
    
#
class Dog(Animal):
    
    def __init__(self, name):
        self.name = name

sa = Dog("Ss")
sa.print_name()
