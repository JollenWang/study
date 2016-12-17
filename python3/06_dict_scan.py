#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

favorite = {'Jollen' : 'Python', 'Jeff' : 'C', 'Bob' : 'Java', 'Sherry' : 'C++', 'Alex' : 'Ruby', 'Musk' : 'GO'}
print("Origin dictonary is:" + str(favorite))

for name, favo in favorite.items():
    print(name.title() + "'s favorite language is " + favo)

print('\nkeys:')
for key in favorite.keys():
    print(key.title())

print('\nvalues:')
for v in favorite.values():
    print(v)
