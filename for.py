for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')



#By default, range takes a step count of 1. If we supply a third number to range, then that becomes the step count.
for i in range(1,5,2):
    print(i)
else:
    print('The for loop is over')

#List, count all numbers
for i in list(range(5)):
    print(i)
else:
    print('The for loop is over')
