#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

p0 = {
    'ID' : 'jollen', 
    'Age' : 32, 
    'Favorite' : ['C', 'Python', 'Java', 'ASM']
}
p1 = {
    'ID' : 'alex', 
    'Age' : 30, 
    'Favorite' : ['Java']
}
p2 = {
    'ID' : 'tom', 
    'Age' : 40, 
    'Favorite' : ['Ruby', 'PHP']
}

dict_list = [p0, p1, p2]
print("dict_list: " + str(dict_list))

print("")
for p in dict_list:
    print(p['ID'].title() + "'s age is " + str(p['Age']) + ", he/her's favorite is :")
    for l in p['Favorite']:
        print('\t' + l)

print("Done.")
