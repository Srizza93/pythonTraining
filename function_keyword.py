#When value is missing, it get the one on the function.
#a,b,c are default values. I.E. 3,7 are keywords arguments.

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

print("\n")

#PRACTICE
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
#In this case, 3 represents a, 7 represents b, 9 represents c.
func(3, 7, 9)
func(25, c=24)
func(c=50, a=100)
