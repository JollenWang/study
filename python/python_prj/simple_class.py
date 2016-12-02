#!/usr/bin/python

# demo of simple class

class person:
    pass

p = person()
print(p)
print('p2=', p)

class Tag:
    def sayHi(self):
        print('Hi,how are you?')

p = Tag()
p.sayHi()
print(p)

