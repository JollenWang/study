#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

class MyClass(object):
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
    """
    return [obj]

