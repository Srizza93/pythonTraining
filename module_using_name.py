if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

#If program is run by another module, you will see the following:
    #$ python
#>>> import module_using_name
#I am being imported from another module
#>>>
