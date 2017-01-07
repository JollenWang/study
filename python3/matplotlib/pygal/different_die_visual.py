#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import pygal
from die import Die

die = Die()
die2 = Die(10)
results = []

for roll_num in range(5000):
	result = die.roll() + die2.roll()
	results.append(result)

frequencies = []
max_result = die.num_sides + die2.num_sides
for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('../saves/different_die_visual.svg')

