#!/usr/bin/python

# File name: using_dict.py

addr_book = {
    'Swaoop': 'swaoop@edu.cn',
    'Jony': 'jony@edu.cn',
    'Marry': 'marry@edu.cn'
}

print('Marry\'s address is %s' % addr_book['Marry'])
print("Jone's address is %s" % addr_book['Jony'])

# adding new key/value pair
print('Add a new address to the book')
addr_book['Jollen'] = 'xkwang@smit.com.cn'
print("Jollen's address is %s" % addr_book['Jollen'])

print('Delete an existed address from the book')
del addr_book['Swaoop']

for name, address in addr_book.items():
    print('Contact %s at %s' %(name, address))

if 'Swaoop' in addr_book:
    print('Swaoop is in the book,%s' % addr_book['Swaoop'])
else:
    print('Swaoop is not exist yet')
