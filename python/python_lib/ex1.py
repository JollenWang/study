#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
Python允许实时创建函数参数列表，把所有参数放入一个数组中，
然后调用内建函数apply.
'''

def fun(a, b):
    print a, b

apply(fun, ("Hello", "Jollen"))
apply(fun, ("Good", "Morning"))
apply(fun, (1 + 2, 6))



