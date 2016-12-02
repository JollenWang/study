#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

class Person:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        print "self=%s" %self
    def sayHi(self):
        print "$>my name is ", self.name
    def getIdx(self):
        print "$>my index is ", self.idx


p = Person("Jollen", 007)
p.sayHi()
p.getIdx()




        
