#!/usr/bin/env python3

print("Welcome to the grade calculator")

# Collect student information
grade1 = int(input("Enter your first grade? "))
grade2 = int(input("Enter your second grade? "))
grade3 = int(input("Enter your third grade? "))

# Calculate the average
average = (grade1 + grade2 + grade3) / 3
print("Your average is", average)

# Logic block
if average <= 10:
    print("FAILED!!!!!")
elif average > 10 and average < 12:
    print("Passable")
elif average >= 12 and average < 13:
    print("Fairly Good")
elif average >= 14 and average < 16:
    print("Good")
else:
    print("Very Good")
print("Thank you using the grade calculator")
print("Come again next time")

