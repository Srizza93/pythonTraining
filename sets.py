''' WHIT "SET" SAME ITEMS CAN BE PRINTED ONLY ONCE, EVEN WRITE THEM TWICE '''

''' RANDOM LIST, NO POSITION SET FOR ANY ITEM'''
# Indeed you need to use the name of the item to add, del etc. not the position ex.[2]

favgames = set(["mario bros 3", "mario kart", "Earthbound", "Pilotwing", "mario kart"])
favgames.add("Zelda")
# favgames.remove("mario kart") This code gives Key Error if we write an item not in the list
favgames.discard("mario kart") # We this code if we misspell the item, it just report the same list without giving error
print(favgames)

print("\n")

numbers = [3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2]

unique = set(numbers)
print(unique)
