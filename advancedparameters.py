def madlib(name, verb, noun):
    print(name + " was " + verb + " with " + noun + "!")

madlib("Nick", "running", "cheese")

print("\n")

def madlib(name="Sean", verb="eating", noun="cheese"):
    print(name + " was " + verb + " with " + noun + "!")

madlib()

print("\n")

def madlib(name, verb, noun, *lastones):
    print(name + " was " + verb + " with " + noun + "!")
    print(lastones)

madlib("Nick", "running", "cheese", 2)
