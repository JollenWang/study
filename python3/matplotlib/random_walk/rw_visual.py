#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

#set window size
plt.figure(dpi = 128, figsize = (10, 6))

#set variable color value for each point
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Reds, edgecolor = 'none', s = 8)

#set start and end point with different color and bigger size
plt.scatter(0, 0, c = 'green', edgecolor = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'blue', edgecolor = 'none', s = 100)

#hide the x axis and y axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.savefig("../saves/random_walk_color2.png", bbox_inches = 'tight')
plt.show()

