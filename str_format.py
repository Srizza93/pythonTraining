#FORMAT METHOD (TEXT WRITING)

#1st method
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#2nd method
age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

#3rd method
age = 20
name = 'Swaroop'

print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='')
print('b', end='')

#Escape "per andare a capo"
print("\n")

print('a', end=' ')
print('b', end=' ')
print('c')

#Escape n°2 "per andare a capo"
print("Hello World\n")

#Escape n°3 "per andare a capo"
print("a", end=" ")
print("Hello","World")

#Raw string
r"Newlines are indicated by \n"

print("name_2_3")
