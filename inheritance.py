class Dog:
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def barkhello():
        print("Hello World")

    def barkgoodbye(self):
        print("Goodbye")

class Bulldog(Dog):
    def growl(self):
        print("GRRRRRRRRRRR")

dog1 = Bulldog("Mike", 22, "White")
print(dog1.name)
dog1.barkgoodbye()
dog1.growl()

print("\n")

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2016 - self.year

class Mustang(Car):
    def __init__(self, year):
        self.year = year
        self.make = "Ford"
        self.model = "Mustang"

