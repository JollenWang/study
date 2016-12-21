#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

class pet():
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def tell_info(self):
        print("pet kind:%s, name is %s, age is %d." %(self.kind, self.name.title(), self.age))

    def roll_over(self):
        print(self.name.title() + " roll over!")

if __name__ == "__main__":
    pet0 = pet("Dog", "Jack", 2)
    pet1 = pet("Rabit", "Apple", 1)

    pet0.tell_info()
    pet0.roll_over()
    pet1.tell_info()
    pet1.roll_over()
