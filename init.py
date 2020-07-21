class Dog:
    # Below. This is a method (which is a function in a class)
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor


dog1 = Dog("Fido", 8, "Brown")

print(dog1.name)
