#Return function. If function. Depending on maximum between the two values, it returns the result.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

print("\n")

#If you don't insert the value, it is same as returnNone, which it means literally nothing.
#Indeed is result is nothing
def maximum(x, y):
    if x > y:
        return
    elif x == y:
        return 'The numbers are equal'
    else:
        return

#This is a None function
print("\n")

def some_function():
    pass


