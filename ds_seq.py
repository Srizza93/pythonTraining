#Fiscal code generator possible with this formula

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swarolp'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])   #It starts counting from the end  (-1 = 3)
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])  # 3 it's not included, to print it, it would be: [1:] ('to end' as below)
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])  #In this case, logic is same (0, '1', '2') 3 = -1 is not included
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])   #Same as above, but to 3 it would be: [1:4]
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1]) #Same as above, but here (0, '1', '2', '3', '4', '5') 6 = -1 is not included
print('characters start to end is', name[:])

#Practice
print('characters start to -1 is', name[:-1]) #Here we count numbers till -1 not included)
print('characters end to start', name[::-1])  #Here we count all with decreasing order
print('characters multiples of 2 starting from end', name[::-2])  # 6, 4 , 2, 0
print('characters multiples of 3 starting from end', name[::-3])  # 6, 3, 0
print('characters multiples of 4 starting from end', name[::-4])  # 6, 2
print('characters multiples of 5 starting from end', name[::-5])  # 6, 1
print('characters multiples of 6 starting from end', name[::-6])  # 6, 0
print('characters start to end 2nd version', name[::1])   #Here we count all with increasing order
print('characters multiples of 2', name[::2])  # 0, 2, 4, 6
print('characters multiples of 3', name[::3])  # 0, 3, 6
print('characters multiples of 4', name[::4])  # 0, 4
print('characters multiples of 5', name[::5])  # 0, 5
print('characters multiples of 6', name[::6])  # 0, 6
print('Item end to start', shoplist[::-1])  #Here we count all with decreasing order
print('Item start to end 2nd version', shoplist[::1])   #Here we count all with increasing order
print('Item 0 and 2', shoplist[::2])   #Here we count 0, 2
print('Item 0 and 3', shoplist[::3])   #Here we count 0, 3

print("\n")

#Text reverser with bold and in loop
BOLD = '\033[1m'
END = '\033[0m'

print('{}'.format(BOLD))
print('TEXT REVERSER')
print('{}'.format(END))
print('\n')
while True:
    s = input('Tap your name: ')
    print('The contrary of your name is: ', s[::-1])
    if s == 'quit':
       break

print('\n')

#BOLD = '\033[1m'
#END = '\033[0m'

#print('{}'.format(BOLD))
#print('TEXT REVERSER')
#print('{}'.format(END))
#print('\n')

#import os
#import sys

#def textrev():
 #   s = input('Tap your name: ')
  #  print('The contrary of your name is: ', s[::-1])

#if __name__ == '__main__':
 #   textrev()
  #  os.execv(__file__, sys.argv)

print('\n')

#Guess the word
while True:
    s = input('Which is the capital of Italy? ')
    if s == 'Roma':
        break
        print('Congratulations!!!, Now we go to the next question')


print('\n')

while True:
    s = input('Which is the capital of France? ')
    if s == 'Paris':
        break
        print('You won!!!!')

