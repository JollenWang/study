#!/usr/bin/python
# Demo of using tuple

zoo = ('wolf', 'elephant', 'tiger', 'monkey', 'eagle')
new_zoo = ('horse', 'cat', zoo)
print('Number of animals in the zoo is:', len(zoo))
print('Number of animals in the new zoo is:', len(new_zoo))

print('All animals in the new zoo are:', new_zoo)
print('Animals brought from old zoo are:', new_zoo[2])
print('The last animal in the old zoo is:', new_zoo[2][4])

# Demo of print tuple
name='Swaroop'
age = 22
print('%s\'s age is %d years old' %(name, age))
