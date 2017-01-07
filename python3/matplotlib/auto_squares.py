#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

#plt.scatter(x_values, y_values, edgecolor = 'none', s = 50)
#plt.scatter(x_values, y_values, c= 'red', edgecolor = 'none', s = 50)
plt.scatter(x_values, y_values, c= (0.8, 0, 0), edgecolor = 'none', s = 50) #use RGB mode

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Number", fontsize = 14)
plt.ylabel("Square", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.axis([0, 1100, 0, 1100000])

plt.savefig('./saves/auto_squares.png', bbox_inches = 'tight')
plt.show()

