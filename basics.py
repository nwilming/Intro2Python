'''
Introduction to python: Basic language concepts
'''

'''
No. 1: Dynamic typing
'''

a_number = 1  # Variable a_number now holds the number 1
a_number = a_number + 10
print(a_number)

a_number = '1'  # Variable now holds a string!
a_number = a_number + 10  # Does not work

a_string = str(10) + '1'
print(a_string)


'''
No. 2: Control flow
'''
a_string = '101'
a_number = 11

if a_string == '101':
    print('a_string is 101')
elif a_number == 11:
    print('a_number is 11')
else:
    print('Nah')

# No switch / case statement!

a_number = 11
for i in range(a_number):  # for loops through any iterable
    a_number += 10
print(a_number)


while a_number > 10:
    a_number -= 1
print(a_number)


try:
    a_number = a_number + '10'  # Does not work
except TypeError as e:
    print('Cant\'t add number to string')
    a_number = a_number + 10
finally:  # Now matter what, always do this
    pass


'''
No. 3: Data structures
'''

# Lists:

a_list = ['foo', 'bar', 'un']
print(a_list)
a_list.append('fug')
print(a_list)
a_list.extend(['foz', 'baz'])
print(a_list)
print(a_list + [1, 2, 3])
print(a_list * 2)

# How to index lists: Index starts at 0!
print(a_list[0])  # foo
print(a_list[1])  # bar

print(a_list[-1])  # baz
print(a_list[-2])  # foz

# Indices:
#  foo bar un  fug foz baz
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

del a_list[-1]
print(a_list)
a_list.insert(0, -1)  # Insert -1 at front
print(a_list)

# Lists are references

a = b = [1, 2, 3, 4]
a.extend([5])
print(b)

for i in b:
    print(i)

# Tuples:

a_tuple = (1, 2, 3, 4)
print(a_tuple)

a_tuple[1] = -1

not_a_tuple = (1)
print(not_a_tuple)

# Dictionaries:

a_dict = {'one':1, 'two':2, 'three':3}
print(a_dict)
a_dict['one'] = 2
a_dict['foo'] = 'bar'
print(a_dict)

a_dict.update({'un':'fug', 'baz':'bar'})
for key, item in a_dict.items():
    print(key, item)

for key in a_dict.keys():
    print(key, a_dict[key])

for item in a_dict.values():
    print(item)


# Something fun: List and dictionary comprehensions

fibonacci = [1, 1, 2, 3, 5, 8, 13, 21]