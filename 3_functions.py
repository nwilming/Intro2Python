'''
Functions
'''


def foo(x):
    '''
    This function computes the square of x.
    '''
    return x**2


print(foo(10))

help(foo)  # Display the doc string.


def foo(x):  # Functions can return multiple values
    return x**2, x**4, x**8

print(foo(10))
print(type(foo(10)))

x2, x4, x8 = foo(10)  # Tuple unpacking!


def foo(x):  # Returns None when nothing is returned
    pass

print(foo(10))


def foo(argument1, argument2):  # Functions can take many input arguments
    return argument1**argument2

print(foo(2, 4))


def raise_x(exponent, x=2): # With one default argument.
    return x**exponent

print(raise_x(8))
print(raise_x(8, x=8))  # Overwrite default value
print(raise_x(x=7, exponent=8))
print(raise_x(7, 8))


# *args and **kwargs
def foo(x,y):
    return x*y
print(foo(3,4))
print(foo(3,4,2))

# With *args you can create more flexible code that accepts a varied amount of non-keyworded arguments within your function:
def foo(*args):
    print(args)
    
print(foo(3,4,2))

def foo(*args):
    z = 1
    for num in args:
        z *= num
    return z
print(foo(3,4,2))

def foo(base, *args): # possible to combine normal arguments with *args
    return [base**a for a in args]
foo(2, 1, 2, 3, 4)

# **kwargs works the same, but now one has to provide keywords.
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(1, 2, 3, key1='value', key2='value2')


# Do something more fancy: Print a spiral to the console
# and use two functions for this.

def spiral_distance(x, y, alpha=5, beta=2, max_dist=100):
    '''
    Return distance to closest spiral arm
    '''
    from math import atan2, pi
    r = (x**2 + y**2)**.5
    theta = atan2(y, x)
    distance = min(
        [abs((r - (alpha + beta * theta + rev * beta * pi * 2)))
         for rev in range(0, max_dist)])
    return distance


def print_spiral(nx, ny, dt=0.5, **kw):
    for x in range(-nx, nx):
        for y in range(-nx, ny):
            r = spiral_distance(x, y, **kw)
            if r < dt:
                print('# ', end='')
            else:
                print('_ ', end='')
        print('')

print_spiral(10, 10, dt=1, beta=1, alpha=0,)
print_spiral(10, 10, dt=1, beta=1, alpha=0, max_dist=2)


# Functions are objects

foo = print_spiral
foo(10, 10, dt=1, beta=1, alpha=0)

# This enables several really nice things:
def print_distance(func, nx, ny, dt=0.5, **kw):
    for x in range(-nx, nx):
        for y in range(-nx, ny):
            r = func(x, y, **kw)
            if r < dt:
                print('# ', end='')
            else:
                print('_ ', end='')
        print('')


print_distance(spiral_distance, 10, 10)


# Simple functions:
foo = lambda x,y: spiral_distance(x, y, beta=0.5)
print_distance(foo, 10, 10, dt=1)


# But also the following pattern:

def log(func):
    def foo(*args, **kw):
        print('Calling function', func.__name__)
        return func(*args, **kw)
    return foo

print_distance = log(print_distance)
print_distance(spiral_distance, 10, 10)

# This is called the decorator pattern and there  is 
# some syntax sugar for it:

@log
def print_distance(func, nx, ny, dt=0.5, **kw):
    for x in range(-nx, nx):
        for y in range(-nx, ny):
            r = func(x, y, **kw)
            if r < dt:
                print('# ', end='')
            else:
                print('_ ', end='')
        print('')

print_distance(spiral_distance, 10, 10)
