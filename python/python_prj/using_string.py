#!/usr/bin/python

# file name: using_string.py

name = 'hello world'

if name.startswith('hel'):
    print('string is start with hel')

if 'o' in name:
    print('o is in string name')

if name.find('rl') != -1:
    print('rl is found in the string')

mylist = ['google', 'microsoft', 'apple', 'alibaba', 'tensence']
link = '<->'
print('join link with string = ', link.join(mylist))
