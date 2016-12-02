#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
demo of lambda
'''

maximum = lambda x,y: (x>y)*x + (x<y)*y
minimum = lambda x,y: (x<y)*x + (x>y)*y

def test():
    x = int(raw_input("$>input x:"))
    y = int(raw_input("$>input y:"))
    print("The larger one is %d" %maximum(x, y))
    print("The little one is %d" %minimum(x, y))

test()






