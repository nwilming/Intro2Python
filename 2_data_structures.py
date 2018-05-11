
'''
Data structures
'''

# Lists:

alist = ['foo', 'bar', 'un']
print(alist)
alist.append('fug')
print(alist)
alist.extend(['foz', 'baz'])
print(alist)
print(alist + [1, 2, 3])  # Concatenate
print(alist * 2)  # repeat

# How to index lists: Index starts at 0!
print(alist[0])  # foo
print(alist[1])  # bar

print(alist[-1])  # baz
print(alist[-2])  # foz

# Indices:
#  foo bar un  fug foz baz
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

del alist[-1]
print(alist)
alist.insert(0, -1)  # Insert -1 at front
print(alist)

alist[::2]
alist[::-2]
alist[::-1]


# Lists are references / mutable

a = b = [1, 2, 3, 4]
a.extend([5])
print(b)

# Immutable types do not have this behavior
a = b = 1
b = b + 1  # Creates new object.
print a

# Logical operators:
a = b = [1, 2, 3, 4]
a is b

a, b = [1, 2], [1, 2]
a is b

a = b = 1
a is b

b = b + 1
a is b


if 1 in [1, 2, 3]:
    print('1 is in list')

if 5 not in [1, 2, 3]:
    print('5 is not in list')


'''
Interlude: Lists/Collections and for loops

'''

a, b = [1, 2]  # Inconspicuous but really cool
b, a = a, b

for i, elem in enumerate(alist):  # Use enumerate to get counter
    print(i, elem)


# Introduce zip

for index, elem in zip(range(len(alist)), alist):  # Zip two lists together!
    print(index, elem)
list(zip(range(len(alist)), alist))
list(zip(alist, alist))
list(zip(alist[:-1], alist[1:]))


from itertools import product
for a, b in product([1, 2, 3], ['A', 'B', 'D']):  # Flattens nested for loops
    print(a, b)


'''
Continue with data structures

Tuples: Immutable lists (advantage: fast)
'''


atuple = (1, 2, 3, 4)
print(atuple)

atuple[1] = -1

not_a_tuple = (1)
print(not_a_tuple)


'''
Dictionaries:
'''

adict = {'one': 1, 'two': 2, 'three': 3}
print(adict)
adict['one'] = 2
adict['foo'] = 'bar'
print(adict)

adict.update({'un': 'fug', 'baz': 'bar'})
for key, item in adict.items():
    print(key, item)
list(adict.items())

for key in adict.keys():
    print(key, adict[key])

for item in adict.values():
    print(item)


# Something fun: List and dictionary comprehensions

[x**2 for x in range(1, 100, 10)]

[x**2 for x in range(1, 100, 10) if (x**2 / 2) > 100]

[(x, y) for x, y in zip(range(10), range(1, 10))]

[['#' if x > y else '.' for x in range(10)] for y in range(10)]

# Use instead of very simple for loops

{a: b for a, b in zip(atuple, ['a', 'b', 'c', 'd'])}
