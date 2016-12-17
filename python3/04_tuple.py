#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

dimensions = (100, 390, 20)
print("origin tuple: " + str(dimensions))

for n in dimensions:
    print(n)

print("print by index:")
for i in range(0, len(dimensions)):
    print(dimensions[i])

print("\nRedefine the tuple:")
dimensions = (15, 27)
print("The new tuple is: " + str(dimensions))


print("Try to modify a tuple item:")
dimensions[1] = 99
