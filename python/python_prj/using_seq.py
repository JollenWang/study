#!/usr/bin/python

# File name: using_seq.py

shoplist = ['apple', 'pear', 'book', 'oil', 'cloth', 'sugar']

count = len(shoplist)
print('size of shoplist is %d' % count)
print('size of shoplist is', shoplist.__len__())
print('size of shoplist is %d' %(shoplist.__len__()))
print('size of shoplist is', list.__len__(shoplist))
print('size of shoplist is %d' %(list.__len__(shoplist)))

for name in shoplist.__iter__():
    print('Item is %s'% name)

for i in shoplist:
    print('item[%d] is %s' %(shoplist.index(i), i))

print('item[-1] is', shoplist[-1])
print('item[-2] is', shoplist[-2])
print('item[-3] is', shoplist[-3])
print('item[-4] is', shoplist[-4])
print('item[-5] is', shoplist[-5])
# print('item[-7] is', shoplist[-7]) # out of range

print('item 1 to 3 is', shoplist[1:3])
print('item 1 to 4 is', shoplist[1:4])
print('item 1 to 5 is', shoplist[1:5])
print('item 1 to 7 is', shoplist[1:7])
print('item 1 to 9 is', shoplist[1:9])
print('item all is', shoplist[0: shoplist.__len__()])
print('item all is', shoplist[:])

