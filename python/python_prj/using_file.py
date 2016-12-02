#!/usr/bin/python

# demo of using file

title = '''\
<<-------------------------------------
Programming is fun when the work is done
if you wanna make your work also fun:
    using python!
------------------------------------->>
'''

f = open('demo.txt', 'w') #open file with write mode
f.write(title)
f.close()
########################################################

f = open('demo.txt') #default open mode is read
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()