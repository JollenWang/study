#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：求1+2!+3!+...+20!的和
'''

sum = 0
base = 1

for i in range(1, 21):
    base *= i
    sum += base

print("1+2!+3!+...+20!=%ld" %sum)


