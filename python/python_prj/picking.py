#!/usr/bin/python
# File name: pickling.py

import _pickle as p

title = 'shoplist.data'
shoplist = ['mango', 'apple', 'carrot']

# write to the file
f = open(title, 'w')
# p.dump(shoplist, f) #dump the object to a file
f.close()

del shoplist
f = open(title)
storedlist = p.load(f)
print(storedlist)
