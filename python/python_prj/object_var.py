#!/usr/bin/python

# using of object variable

class Person:
    '''Represent a person'''
    population = 0

    def __init__(self, name):
        '''Initialize the persion's data'''
        self.name = name
        print('initialize %s' % self.name)
        Person.population += 1

    def __del__(self):
        '''I am leaving'''
        print('%s says bye' %self.name)
        Person.population -= 1

        if Person.population == 0:
            print('I am the last one')
        else:
            print('The are %d person left' %Person.population)

    def sayHi(self):
        '''Greeting by the person.
        Really,that's all it does.'''
        print('Hi, my name is %s' %self.name)

    def howMany(self):
        '''Print the current population'''
        print('There are %d person here.' %self.population)

    def __add__(self, other):
        '''Add person to the object'''
        self.name = other
        Person.population += 1
        print('Add a person,total: %d,last name: %s' %(self.population, self.name))

a = Person("Alpha") # init is called
#a.sayHi()            # sayHi() is called
#a.howMany()          # howMany() is called

b = Person('Elson')

"""
a.__init__("Jollen")
a.__init__('Guoguo')
a.__init__('June')
a.__del__()
a.__del__()
a.__del__()
a.__del__()
a.__add__('A')
a.__add__('B')
a.__add__('C')
#a.sayHi()
"""

