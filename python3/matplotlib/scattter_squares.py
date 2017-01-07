#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6]
y_values = [1, 4, 9, 16, 25, 36]
plt.scatter(x_values, y_values, s = 100)
#plt.scatter(2, 4, s = 200)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Number", fontsize = 14)
plt.ylabel("Square", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

