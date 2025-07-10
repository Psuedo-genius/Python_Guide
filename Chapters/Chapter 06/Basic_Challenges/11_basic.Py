# Use if-elif-else to assign letter grades
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks >= 85 and marks <= 89:
    grade = 'B+'
elif marks >= 80 and marks <= 89:
    grade = 'B'
elif marks >= 70 and marks <= 69:
    grade = 'C'
elif marks >= 60 and marks <= 59:
    grade = 'D'
elif marks > 100:
    print("Invalid marks. Please enter a number between 0 and 100. \
            \nHahaha what a fool thinks he can score higher than 100! :")
    exit()
else:
    grade = 'F'

print(f"Your grade is: {grade}")
# line 13 to 16 was just added for the fun chill guys
