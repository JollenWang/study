#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input("Enter-->")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)

except EOFError:
    print "No EOF at end!"
except ShortInputException, x:
    print 'ShortInputExcept:inupt len %d,but %d wangted!' %(x.length, x.atleast)
else:
    print "No exception was raised!"
