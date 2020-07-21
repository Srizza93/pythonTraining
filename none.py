


def searchstring(search):
    return None

print(searchstring(""))
print("\n")

def square(number):
    if number != float(number):
        print("Hello")
        return None
    elif number != int(number):
        print("Hello")
        return None
    else:
        return (number*number)

print(square(5))
print("\n")

def square(number):
    if  str(type(number)) == "<class 'int'>":
        return number * number
    elif  str(type(number)) == "<class 'float'>":
        return number * number
    else:
        return None
#Test
print(square(5))
print(square(5.0))
print(square("It should return None"))
