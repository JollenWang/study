#!/usr/bin/python
# Function:using list

# The fruit list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to buy!\n')
print('The items are:',)
for i in shoplist:
    print(i)

print('I also have to buy rice')
shoplist.append('rice')
print('The new shoplist is now:', shoplist)

shoplist.sort()
print('The shoplist after sort:', shoplist)

del shoplist[1]
print('The shoplist after del item[1]:', shoplist)
