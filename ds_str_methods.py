# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

print('\n')

name = '1234567890,3858274927,9848328457,4667343183'
# Indexing or 'Subscription' operation #
print('Item 0 is', name[0:10],name[11:21],name[22:32],name[33:43])
print('Item 0 is', name[6:11])
print('Item 0 is', name[12:17])

print('\n')

delimiter = ' '
mylist2 = input('Tap here: ')
print(delimiter.join(mylist2))

print('\n')

s = input('Tap here: ')
s = s.replace(',', '')
print(s)

print('\n')

s = input('Tap here: ')
s = s.replace(',', ' ')
print(s)

print('\n')

with open('ds_str_methods.py') as infile, open('output', 'w') as outfile:
    outfile.write(infile.read().replace(",", "  "))

print('\n')

number = input('Tap here:')
number2 = number.replace(",", " ")
number2 = number.replace(";", " ")
number2 = number.replace("  ", " ")
number2 = number.split()
print(number2)
