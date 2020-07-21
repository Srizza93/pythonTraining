age = 27

while age < 100:
    print(age)
    age += 1 # If this is missing, it's going to print 27 forever

print("\n")

guess = input("Guess a number between 0 and 10: ")

while guess != "8": # 8 can be between strings "8" or we need to add int to guess
    guess = input("Guess a number between 0 and 10: ")

print("You win!")

a = 2 // 1000000000
print(a)

print("\n")

count = 1

while 2**count < 1000000000:
    count += 1

print(count)

