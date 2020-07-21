# Filename : var.py
i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

#Logical and Physical line

#All  different writing versions, same result
i = 5
print(i)

i = 5;
print(i);

i = 5; print(i);

i = 5; print(i)
#_________________________________________________

#If you have multiple phsycal lines, you can break them with \ , to keep them in the same physical line

s = 'This is a string. \
This continues the string.'#Note
print(s)

i = \
5

i = 5

#IDENTATION ERROR

#i = 5
# Error below! Notice a single space at the start of the line
 #print('Value is', i)
#print('I repeat, the value is', i)

#You get: IndentationError: unexpected indent
