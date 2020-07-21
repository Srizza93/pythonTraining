#Doc String. It evaluates the maximum and then provide the doc written at the begin
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

print("\n")

#Without "print(print_max.__doc__)" it doesn't print the doc.
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)

print("\n")

#PRACTICE
#It is adviced to follow the convention of having the first letter as CAPITAL and end the first line with a dot .
#Also second line should be empty, and third will give instructions.
#It actually works without following the convention.
def print_max(x, y):
    '''prints the maximum of two numbers
    the two values must be integers'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

