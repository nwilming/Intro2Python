'''
Packages, modules and so forth.
'''

import math
# math.tabcomplete

math.sin(math.pi)

from math import sin
from math import sin as sinus
from math import sin as sinus, cos

from math import *  # Behold the star is for gods only.
# Only acceptable * import is from pylab import *

import foobar
help(foobar)

import sys
_ = [print(s) for s in sys.path]

# Show how to make own package.
# --> foobar example, python setup.py

# A tour of the most important standard packages:
import os  # Access to pathes
os.getcwd()

import shutil  # top copy/move/delete files

from glob import glob
glob('*.py')


import sys  # Get command line arguments
# sys.argv

import re  # Regular expressions and string pattern matching

import pickle

pickle.dump({'save': 'a dictionary'}, open(
    'tmp.pickle', 'wb'))  # Needs to be binary writing
print(pickle.load(open('tmp.pickle', 'rb'))
# Caveat: classes must be importable


# OOP
# Everything is an object in Pythob

class Something(object):

    shared_between_classes=['This is shared between']

    def __init__(self, x):
        self.x=x

    def do(self):
        print(self.x)


book=Something('Book')
book.do()
print(book.shared_between_classes)


glasses=Something('Glasses')
glasses.shared_between_classes[0]='Yes indeed!'
print(book.shared_between_classes)

# Asking for forgiveness
try:
    read_book = glasses + book
except TypeError:
    pass

# Is better than 'Look before you leap'
if isinstance(glasses, Something) and isinstance(book, Something):
    print ('glasses and book are Something')


class Something(object):

    shared_between_classes=['This is shared between']

    def __init__(self, x):
        self.x=x

    def do(self):
        print(self.x)

    def __add__(self, x):
        return Something(self.x + x.x)

    def __repr__(self):
        return self.x

glasses=Something('Glasses')
book=Something('Book')
read_book = glasses + book

# Other operators: mul, sub, mod, lt, le, eq, ne, gt, ge, getitem, contains,
# len, str


# Other loose ends:

# String formatting:
print('{} is {} format a string'.format('This', 'how to'))
print('{0} is {1} format a string'.format('This', 'how to'))
print('{1} is {0} format a string'.format('This', 'how to'))
print('But {who}  can also use {what}'.format(who='you', what='keywords'))
print('But {who}  can also use {what}'.format(**{'who':'you', 'what':'dicts'}))

print('Format can also style numbers: {:2.3f}'.format(0.0125049421))

x=range(20)
for vals in zip(x[0::3], x[1::3], x[2::3]):  # Neat trick
    print('{:03d} {:03d} {:03d}'.format(*vals))

'This is the old style: %03.4f' % (0.1234)

value=0.12423532
f"And this is the future: {value:{3}.{4}}"


# Reading/Writing files:

f=open('test.txt', 'w')  # w makes file writable
for s in ['a', 'b', 'c', 'd']:
    f.write(s + '\n')
f.close()

f=open('test.txt', 'r')  # File is readable only
for line in f:
    print(line, end='')
f.close()


# Better:
with open('test.txt', 'r') as f:  # Context manager will
                                  # automatically close file after block
    for line in f:
        print(line, end='')

# Autoreload

# Generators and yield

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

t=reverse([1, 2, 3, 4])

for i in t:
    print(i)



# unicode in python 3:
astring = b'abc'.decode('utf-8') 
somebytes = astring.encode('utf-8')



# The Zen of python
import this
