favgames = ["mario bros 3", "Earthbound", "Pilotwing", "mario kart"]

print(favgames[2])

print("\n")
''' ADVANCED LISTS'''
''' APPEND, INSERT, UPDATE, DELETE AND LENGHT'''

favgames2 = ["mario bros 3", "Earthbound", "Pilotwing", "mario kart"]

favgames2.append("Zelda")
favgames2.insert(2, "Donkey Kong") # Insert item in the preferred position
print(favgames2)

print("\n")

favgames = ["mario bros 3", "Earthbound", "Pilotwing", "mario kart"]

favgames[2] = "Zelda" # Insert item in the preferred position
del(favgames[0]) # DELETE POSITIONAL ITEM
print(favgames)

print("\n")

favgames = ["mario bros 3", "Earthbound", "Pilotwing", "mario kart"]

favgames.remove("Pilotwing") # DELETE ACTUAL TERM ITEM
print(len(favgames)) # PRINT LENGHT OF LIST

print("\n")

shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]
newshoes = ("White Vans")

def addtofront(shoes, newshoes):
    shoes.insert(0, newshoes)
    print(shoes)

addtofront(shoes, "White Vans")
