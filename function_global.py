#In this case x is Global, so when you change the value of x, this will be perament till next change.
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

print("\n")

x = 50


def func():
    global x

#Always write in the same block when making changes.
    print('x is', x)
    x = 2
    print('Changed global x to', x)
    x=4
    print('and now x is', x)


func()
print('Value of x is', x)

print("\n")

#PRACTICE, muliple values and multime sentences in the same physical line.
x = 50


def func():
    global x, y, z, a

#Always write in the same block when making changes.
    print('x is', x)
    x = 2
    print('Changed global x to', x)
    x=4
    print('And now x is', x)
    z=3
    print('Instead z is', z)
    y=1
    print('Also y is', y, 'and z is again', z)#two sentences(formula) in the same string
    a=9
    print('And finally a is', a)
    x=4
    print("This time x is ", x)


func()
print('Value of x is', x)
