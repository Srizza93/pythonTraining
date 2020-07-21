def addtwo(num1, num2) -> int:
    thenum = num1 + num2
    return thenum

thenum = addtwo(3, 2)
print(thenum)

print("\n")

'''def printtype(num1):
    if num1 is str:
        return ("String")
    elif num1 is int(num1):
        return ("Int")
    elif num1 is float(num1):
        return ("Float")

num1 = (2)
printtype(num1)

printtype()'''

print("\n")


def printtype(par) -> int or str or float:
    if par == str(par):
        return print("String")
    elif par == int(par):
        return print("Int")
    elif par == float(par):
        return print("Float")

printtype(3.4)


print("\n")

def printtype(param):
    if type(param) == type("Hello"):
        return "String"
    if type(param) == type(12):
        return "Int"
    if type(param) == type(5.8):
        return "Float"
