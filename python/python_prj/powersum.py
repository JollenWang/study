#!/usr/bin/python
#Filename: powersum.py

#import sys
#import os

def powersum(power, *args):
	'''Return the sum of each argument raised to specified power'''
	total=0
	for i in args:
		total += pow(i, power)
	return total

print("#>total=%d" %powersum(2, 1, 2, 3, 4))
