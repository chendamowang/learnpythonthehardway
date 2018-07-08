# -*- coding: utf-8 -*-
# creat a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'Nwe York': 'NY',
    'Michigan': 'MI'
}

# creat a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY states has: ", cities['NY']
print "OR states has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abberviation is: ", states['Florida']

# doing it by using state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbrevation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbrevated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do it at a same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print " Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city

