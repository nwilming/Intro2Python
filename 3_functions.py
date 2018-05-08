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


def raise_x(exponent, x=2):
    return x**exponent

print(raise_x(8))
print(raise_x(8, x=8)) # Overwrite default value

