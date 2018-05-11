#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import numpy as np
from random import choice


def prisonser(N=100):
    """
    The riddle: 100 prisoners are in solitary cells, unable to see, speak or
    communicate in any way from those solitary cells with each other. There's
    a central living room with one light bulb; the bulb is initially off. No
    prisoner can see the light bulb from his own cell. Everyday, the warden
    picks a prisoner at random, and that prisoner goes to the central living
    room. While there, the prisoner can toggle  the bulb if he or she wishes.
    Also, the prisoner has the option of asserting the claim that all 100
    prisoners have been to the living room. If this assertion is false (that
    is, some prisoners still haven't been to the living room), all 100
    prisoners will be shot for their  stupidity. However, if it is indeed true,
     all prisoners are set free. Thus, the assertion should only be made if the
    prisoner is 100 percent certain of its validity.

    Before the random picking begins, the prisoners are allowed to get
    together to discuss a plan.  So ---- what plan should they agree on, so
    that eventually, someone will make a correct assertion?

    Question: How can the prisoners tell, with certainty, that all 100 of them
    have visited the central living room with the light bulb?
    """

    counter_ID = 0  # this prisoner is going to count
    counts = 0  # counter's counts (needs to become N-1)
    turns = 0  # keeps track of the number of turns (days) required

    # keeps track of which prisoners have entered the cell
    beenthere = [False for _ in range(N)]
    light = False  # the light is turned off at t=0

    while (counts < N - 1):
        turns += 1
        prisoner = choice(range(N))  # choose a prisoner
        if prisoner != counter_ID:
            if beenthere[prisoner] is False:
                if light is False:
                    light = True
                    beenthere[prisoner] = 1
        if prisoner == counter_ID:
            if light is True:
                light = False
                counts += 1

    return(turns)

nr_prisoners = 100
turns = prisonser(N=nr_prisoners)

print("total turns (days) required: {}".format(turns))

######################


def expected_turns(N=100):
    '''
    Analytical solution for the expected number of turns.

    Intuition:
    In the first round the light switch will definetly change (+1 turns).
    Now the counter has to enter the room (p=1/99, +1/p turns).
    Now N-1 prisoners can change the light switch (p=(N-1)/99, +1/p turns).
    Now the counter has to enter the room (p=1/99, +1/p turns).
    Now N-1 prisoners can change the light switch (p=(N-2)/99, +1/p turns).
    etc.
    '''
    counter_N = N - 1

    return sum([
        1 / (1 / counter_N) +  # Nr. of turns for counter.
        1 / ((N - i) / N)  # Nr. of turns for next prisoner.
        for i in range(counter_N)])
