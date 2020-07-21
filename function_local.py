x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)

#In the 1st sentence x is clearly "50", in the 2nd sentence we assign a new value to x "2". In the 3rd sentence we
#confirm once again that x is "50" by using func(x)
