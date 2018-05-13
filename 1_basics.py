'''
Introduction to python: Basic language concepts
'''

'''
Dynamic typing (types checked on the fly, during execution of commands)
'''

# No need to explicitly declare variable types.
# Instead, Python keeps track of types.

anumber = 1  # Variable anumber holds the number 1
anumber = anumber + 10
print(anumber)
anumber += 10
print(anumber)

astring = '123'  # Variable astring holds a string!
astring += '123'
print(astring)


print(anumber + astring)  # "Type coersion"; fails because Python is strongly typed.
type(anumber)
type(astring)
print(anumber + int('123')) # Can make it work, but only with an explicit cast (e.g. int() or str())
print(str(anumber) + '123')


'''
Control flow
'''
astring = '101'
anumber = 11


astring == '101'  # Comparison operator

if astring == '101':
    print('astring is 101') # No {} or end statements. Code is grouped by indentation. Use 4 spaces and no tabs.

if astring == '101':
    print('astring is 101')
elif anumber == 11:
    print('anumber is 11')
else:
    print('Nah')

# The elif and else statements are not mandatory.
# We can have as many elif statements as we want.

# *** The if... elif... elif... sequence is a substitue for the switch / case statement found in some other languages ***

# Ternary if (a ? b : c --> evaluates to b if the value of a is true, and otherwise to c)
'Yes' if len(astring) == 10 else 'No'


# Other operators:
# Comparison operators:
# <, <=, >, >=, !=, ==
print(10 != 11)


# Logical operators:
if (astring == '101') or (astring == '102'):
    print(True)

# Parentheses provide confirmation of the developer's intent.
# Parentheses reduce the work required to understand the code.

if (astring == '101') and (astring == '102'):
    print('impossible')

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


anumber = 20
while anumber > 10:  # Second loop version
    print(anumber)
    anumber -= 1

# Python's ultimate error handling goal is to let you know that an error has occurred
# Having fulfilled its goal, what happens next is all up to you.
# If you don't specify anything to happen, then a default error message is displayed and the program is ended.
# You can specify any course of action. E.g., print something, fix the error, etc.
# This comes in especially handy during debugging.

# For this purpose Python uses the try / except statement:
# If any code within the try statement causes an error, execution of the code will stop and jump to the except statement.

anumber = 10
astring = '10'

try:
    anumber = anumber / astring
except:
    print("Something went wrong")

# Let's at least print the error, and double check some things:

try:
    anumber = anumber / astring
except Exception as e:
    print(e)
    print("Something went wrong; printing variable types:")
    print(type(anumber))
    print(type(astring))

# Now let's just try to fix the error:

try:
    anumber = anumber / astring
except Exception as e:
    print(e)
    print("Let's cast 'astring' to int and try again:")
    anumber = anumber / int(astring)
 
# Check for a specific type or error:
 
try:
    anumber = anumber / astring
except TypeError as e:
    print(e)
    print("Let's cast 'astring' to int and try again:")
    anumber = anumber / int(astring)
except:
    print("This is absurd!!")

astring = 0
try:
    anumber = anumber / astring
except TypeError as e:
    print(e)
    print("Let's cast 'astring' to int and try again:")
    anumber = anumber / int(astring)
except:
    print("This is absurd!!")


# Add 'finally' statement:

try:
    anumber = anumber / astring
except TypeError as e:
    print(e)
    print("Let's cast 'astring' to int and try again:")
    anumber = anumber / int(astring)
except:
    print("This is absurd!!")
finally:
    print("Saving variables...")


'''
Miscelaneous
'''

# This is a comment

'''
This is a multiline string if you want

'''

'This is "quotes" inside quotes'

"or 'this'"

