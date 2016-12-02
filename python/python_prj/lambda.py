#!/usr/bin/python
#Filename: lambda.py

def make_repeater(n):
	return lambda s:s*n

twice=make_repeater(2)

print("twice(abc)=%s" %twice("abc"))
print("twice(5)=%d" %twice(5))
