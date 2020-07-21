dogs = {"Fido":8, "Sean":17, "Jane":4}
# Instead of having just variables as lists or tuples, here every variable has a key)

print(dogs)
print("\n")

dogs = {"Fido":8, "Sean":17, "Jane":4}
# Instead of having just variables as lists or tuples, here every variable has a key)
# Dictionaries are pre-set, variable can be written only once, and if written twice, it will print the second update

print(dogs["Fido"])
print("\n")

dogs = {8: "Fido", "Sean":17, "Jane":4}
# Dictionaries are pre-set, variable can be written only once, and if written twice, it will print the second update

print(dogs)
print(dogs[8])
print("\n")

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

#cooldictionary = {"Pogo":"Slang for Pokemon Go", "Spange":"To collect spare change, either from couches, passerbys on the street or any numerous other ways and means", "Lie-Fi":"When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"}
# This below needs to connect keys to values of two different lists
cooldictionary =dict(zip(words,definitions))
print(cooldictionary)
