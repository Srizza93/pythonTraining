class Dog:
    # Below. This is a method (which is a function in a class)
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def barkhello():
        print("Hello World")

    def barkgoodbye(self): # If thia function calls the init function, we need to write self in parentheses
        print("Goodbye")


dog1 = Dog("Fido", 8, "Brown")
Dog.barkhello()
dog1.barkgoodbye() # And then use dog1 for .barkhello, instead of Dog as above
print(dog1.name)
print("\n")

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        carage = 2020 - car1.year
        print(carage)


car1 = Car(2016, "Germany", "Opel corsa")
car1.age()
print("\n")

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2016 - self.year
