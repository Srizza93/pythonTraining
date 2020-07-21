import sys

#Find command line arguments
print('The command line arguments are:')
for i in sys.argv:
    print(i)

#Find file path
print('\n\nThe PYTHONPATH is', sys.path, '\n')

print("\n")

#Find current directory of your program
import os; print(os.getcwd())
