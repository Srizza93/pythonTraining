pointspossible = 100
score = int(input("Score: "))
percent = score / pointspossible
print("Percentage is {}".format(percent))
name = input("Name: ")

if 0 <= score <= 59:
    print("{} - F".format(name))
elif 60 <= score <= 69:
    print("{} - D".format(name))
elif 70 <= score <= 79:
    print("{} - C".format(name))
elif 80 <= score <= 89:
    print("{} - B".format(name))
elif 90 <= score <= 100:
    print("{} - A".format(name))

print("\n")

pointspossible = 100
score = 34
percent = round(score / pointspossible, 2)
print("Percentage is {}".format(percent))
studentname = "Nick"
grade = ""

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

print("{} - {}".format(studentname, grade))
