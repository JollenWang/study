#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from random import randint

class Die():
	def __init__(self, num_sides = 6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

