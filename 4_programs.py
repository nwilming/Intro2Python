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


# A tour of the most important standard packages:

import sys  # System c



# Other loose ends:

# String formatting:
print('{} is {} format a string'.format('This', 'how to'))
print('{0} is {1} format a string'.format('This', 'how to'))
print('{1} is {0} format a string'.format('This', 'how to'))

print('Format can also style numbers: {:2.3f}'.format(0.0125049421))

x = range(20)
for vals in zip(x[0::3], x[1::3], x[2::3]): # Neat trick
    print('{:03d} {:03d} {:03d}'.format(*vals))

'This is the old style: %03.4f'%(0.1234)

value = 0.12423532
f"And this is the future: {value:{3}.{4}}"


# Reading/Writing files:

f = open('test.txt', 'w') # w makes file writable
for s in ['a', 'b', 'c', 'd']:
    f.write(s + '\n')
f.close()

f = open('test.txt', 'r') # File is readable only
for line in f:
    print(line, end='')
f.close()


#Better:
with open('test.txt', 'r') as f:  # Context manager will 
                                  #automatically close file after block
    for line in f:
        print(line, end='')

### Autoreload


