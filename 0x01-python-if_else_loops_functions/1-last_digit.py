#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)
last = int(last[-1])
if (last > 5):
    test = 'and is greater than 5\n'
elif (last == 0):
    test = 'and is 0\n'
elif (last < 6 and last != 0):
    test = 'and is less than 6 and not 0\n'
print('Last digit of {} is {} {}'.format(number, last, test))
