#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

users = ['bob', 'alex', 'tom', 'jollen', 'musk']
valid = []

while users:
    current = users.pop()
    valid.append(current)
    print('Verify user:', current)

print("The following users are verified:")
for u in sorted(valid):
    print('\t', u.title())

