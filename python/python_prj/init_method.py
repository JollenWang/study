#!/usr/bin/python

# using init method

class Person:
    def __init__(self, str):
        self.name = str
    def sayHi(self):
        print('Hi, my name is ', self.name)

king = Person('Jollen')
king.sayHi()

Person('Jollen').sayHi()
