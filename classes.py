class Dog:
    "Hello"

dog1 = Dog()
dog1.name = "Fido"
dog2 = Dog()
dog2.name = "Sean"
dog3 = Dog()

print(dog1.name)

print("\n")

class Dog2:
    doginfo = "Dogs are aninmal with 4 legs and a tail"

dog1 = Dog2()
dog1.name = "Fido"
dog2 = Dog2()
dog2.name = "Sean"
dog3 = Dog2()

print(dog1.doginfo)
print(dog2.doginfo)

print("\n")

class Dog2:
    doginfo = "Dogs are aninmal with 4 legs and a tail"
# Below. Update and delete previous variable
Dog2.doginfo = "Hello"

print(Dog2.doginfo)
print(Dog2.doginfo)
