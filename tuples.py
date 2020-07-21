''' TUPLE IS A LIST THAT CAN'T BE CHANGED '''

'''favgames = ["mario bros 3", "Earthbound", "Pilotwing", "mario kart"]

      ONLY DIFFERENT WITH LIST IS SQUARE BRACKETS [], INSTEAD FOR TUPLE ()
'''

favgames = ("mario bros 3", "Earthbound", "Pilotwing", "mario kart")

# it is not possible to append, delete etc.
print(favgames[2])

print("\n")
'''
shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")
value = "Nike",

def appendtotuple(thetuple, value):
    thetuple = shoes + value
    return thetuple


thetuple = appendtotuple(shoes, value)
print(thetuple)
'''

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5", value)
    return shoes

print(appendtotuple(shoes, "shksvksd"))
