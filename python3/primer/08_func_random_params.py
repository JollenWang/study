#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def say_hello(*namelist):
    print(say_hello.__name__)
    print('Hello, ' + str(namelist))


if __name__ == '__main__':
    say_hello('Jollen', 'Alex')
    say_hello('Tom')
