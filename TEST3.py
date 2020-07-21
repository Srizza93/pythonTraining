class Workers:
    """Represents working staff."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))


        # When this person is created, the robot
        # adds to the population
        Workers.population += 1

    def dismissal(self):
        """I am dying."""
        print("{} has been dismissed".format(self.name))

        Workers.population -= 1

        if Workers.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} workers left.".format(
                Workers.population))

    def say_hi(self):
        """Greeting by your workers.

        Yeah, they can do that."""
        print("Greetings, my name is {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} workers.".format(cls.population))


employee1 = Workers(input('Tap your name: '))
employee1.say_hi()
Workers.how_many()

employee2 = Workers(input('Tap your name: '))
employee2.say_hi()
Workers.how_many()

employee3 = Workers(input('Tap your name: '))
employee3.say_hi()
Workers.how_many()

employee4 = Workers(input('Tap your name: '))
employee4.say_hi()
Workers.how_many()

print("\nWorkers can do some work here.\n")

print("Workers have finished their work. So let's dismiss them.")
employee1.dismissal()
employee2.dismissal()
employee3.dismissal()
employee4.dismissal()

Workers.how_many()
