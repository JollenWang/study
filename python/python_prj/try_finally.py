#!/usr/bin/python
# usage of try...finally

import time

try:
    f = open('demo.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
        time.sleep(1)
finally:
    f.close()
    print('close file:', f.name)
