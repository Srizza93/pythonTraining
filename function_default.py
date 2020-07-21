#It prints the message all the times requested
def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)

print("\n")

def say(message, times=1):
    print(message * times)

say("la", 3)

#For example,def func(a, b=5) is valid, but def func(a=5, b) is not valid.
print("\n")
#PRACTICE
#If times is 5, the if we don't attribute any

def say(message, times=5):
    print(message * times)

say('Hello')
say('World', 5)
