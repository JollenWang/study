#!/usr/bin/python

#file name: using_reference.py

shoplist = ['a', 'b', 'c', 'd', 'e', 'f']
mylist = shoplist

print('shoplist = ', shoplist);
print('mylist = ', mylist);

del shoplist[0]
print('shoplist = ', shoplist)
print('mylist = ', mylist)

# make a copy to mylist
mylist = shoplist[:]

del shoplist[0]
print('shoplist3 = ', shoplist)
print('mylist3 = ', mylist)

