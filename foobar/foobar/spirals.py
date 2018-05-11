#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This module can print spirals!

'''

from math import atan2, pi


def spiral_distance(x, y, alpha=5, beta=2, max_dist=100):
    '''
    Return distance to closest spiral arm
    '''
    r = (x**2 + y**2)**.5
    theta = atan2(y, x)
    distance = min(
        [abs((r - (alpha + beta * theta + rev * beta * pi * 2)))
         for rev in range(0, max_dist)])
    return distance


def log(func):
    def foo(*args, **kw):
        print('Calling function', func.__name__)
        return func(*args, **kw)
    return foo


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

print_distance(spiral_distance
