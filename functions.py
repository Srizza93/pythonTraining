def hello():
    print("Hello World!")
    print("It smells nice outside")
# End of fuction

# Call of function
hello()

print("\n")

def love():
    print("I love python!")

love()

print("\n")

pointspossible = 100
studentname = input("Student name: ")

def calcthegrade(): # Here we can wrap the function and add it when necessary
    percent = round(score / pointspossible, 2)
    grade = "ERROR"

    if 1 >= percent >= 0.9:
         grade = "A"
    elif 0.9 > percent >= 0.8:
         grade = "B"
    elif 0.8 > percent >= 0.7:
         grade = "C"
    elif 0.7 > percent >= 0.6:
         grade = "D"
    else:
         grade = "F"

    print("Percentage is {}".format(percent))
    print("{} - {}".format(studentname, grade))
try:
    score = int(input("Student Score: "))
    calcthegrade() # Here we finally use the function
except Exception:
    print("Please provide valid Number")


