#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def describe_pet(name, type = 'dog'):
    print("I've a pet, name=%s, type=%s" %(name, type))

if __name__ == '__main__':
    describe_pet('Jerry')
    describe_pet('Jafe', 'cat')
