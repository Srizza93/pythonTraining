try:
    age = int(input("Age: "))
    print("Valid number!")
except Exception:
    print("You need to provide a valid number!")

print("\n")

pointspossible = 100
studentname = input("Student name: ")
try:
    score = int(input("Student Score: "))
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
except Exception:
    print("Please provide valid Number")





