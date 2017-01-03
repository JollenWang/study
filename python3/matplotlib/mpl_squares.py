#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

plt.plot(values, squares, linewidth = 5)
plt.title("Squares Number", fontsize = 24)
plt.xlabel("Value", fontsize = 24)
plt.ylabel("Square", fontsize = 24)
plt.tick_params(axis = 'both', labelsize = 24)

plt.show()

