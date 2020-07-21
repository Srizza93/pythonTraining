def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(3, 4)

x = 5
y = 7

#____________________________________________________
#TEST

#2 different formulas. 1st print max between a and b(if formula), the second the max between x and y.
#By writing again formula "print_max(etc." the next formula keep the same comditions (print(a, 'is maximum etc.)
# pass variables as arguments
print_max(x, y)

print("\n")

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(1, 3)

x = 2
y = 2

# pass variables as arguments
print_max(x, y)
