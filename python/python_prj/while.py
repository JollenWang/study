#!usr/bin/python

while True:
    s = input('wait for input...');
    print('you input is', s);
    if s == 'q' or s == 'Q' or s == 'exit':
        print(s, 'break and return');
        break;
    else:
        continue;

def say_hello():
    print('Hello, Jollen!');

def compare():
    a = input('input a');
    b = input('input b');
    if a > b:
        print('a > b');
    elif a == b:
        print('a == b');
    else:
        print('a < b');

say_hello();
compare();