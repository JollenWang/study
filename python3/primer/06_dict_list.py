#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

p0 = {'ID' : 'jollen', 'Age' : 32, 'Favorite' : 'Python'}
p1 = {'ID' : 'alex', 'Age' : 30, 'Favorite' : 'Jave'}
p2 = {'ID' : 'tom', 'Age' : 40, 'Favorite' : 'Ruby'}

dict_list = [p0, p1, p2]
dict_tuple = (p0, p1, p2)

print("dict_list: " + str(dict_list))
print("dict_tuple: " + str(dict_tuple))

for p in dict_list:
    print(p)

for j in dict_tuple:
    print(j['ID'].title() + "'s age is " + str(j['Age']) + " ,favorite is " + j['Favorite'].upper())
