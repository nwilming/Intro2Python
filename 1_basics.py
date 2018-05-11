'''
Introduction to python: Basic language concepts
'''

'''
Dynamic typing
'''

anumber = 1  # Variable anumber now holds the number 1
anumber = anumber + 10
print(anumber)
anumber += 10
print(anumber)

anumber = '231'  # Variable now holds a string!
anumber = anumber + 10  # Does not work

astring = '123'
astring = astring + '123'  # We need explicit cast, python is dynamic but strongly typed

int(astring) + int('123')


'''
Control flow
'''
astring = '101'
anumber = 11


astring == '101'  # Comparison operator

if astring == '101':
    print('astring is 101')  # Code block is indented by 4 spaces

if astring == '101':
    print('astring is 101')  # Code block is indented by 4 spaces
elif anumber == 11:
    print('anumber is 11')
else:
    print('Nah')

# Ternary if
'Yes' if len(astring) == 10 else 'No'


# Other operators:
# Comparison operators:
# <, <=, >, >=, !=, ==
print(10 != 11)


# Logical operators:
if (astring == '101') or (astring == '102'):
    print(True)

if (astring == '101') and (astring == '102'):
    print('impossible')


# No switch / case statement!


for i in [1, 2, 3, 4]:  # for loops through any iterable
    print(i)

for i in range(10):  # Loop until 10, but exclude 10
    print(i)

for i in 'onetwothree':  # for loops through any iterable
    print(i)

for i in 'onetwothree':  # continue skips an iteration
    if i == 't':
        continue
    print(i)

for i in 'onetwothree':  # break terminates the inner most loop
    print(i)
    if i == 't':
        break

for j in [1, 2, 3]:  # But does not completely jump put
    for i in 'onetwothree':
        if i == 't':
            break
        print(i)


anumber = 100
while anumber > 10:  # Second loop version
    anumber -= 1
print(anumber)


try:  # Try except catch exceptions
    foo()
except Exception as e:
    print(e)


try:
    anumber = anumber + '10'  # Does not work
except TypeError as e:
    print('Cant\'t add number to string')
    anumber = anumber + 10

try:
    anumber = anumber + '10'  # Does not work
except TypeError as e:
    print("I don't know what to do!")
    raise(e)


try:
    anumber = anumber + '10'  # Does not work
except TypeError as e:
    print("I don't know what to do!")
    raise(e)
finally:  # Now matter what, always do this
    print('But let me quickly cleanup')


'''
Miscelaneous
'''

# This is a comment

'''
This is a multiline string if you want

'''

'This is "quotes" inside quotes'

"or 'this'"

