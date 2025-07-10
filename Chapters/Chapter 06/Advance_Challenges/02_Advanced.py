# Ask for 3 subject marks → Grade A/B/C/D
subject1 = int(input("Enter the marks for Subject 1: "))
subject2 = int(input("Enter the marks for Subject 2: "))
subject3 = int(input("Enter the marks for Subject 3: "))

# Calculate the average
average = (subject1 + subject2 + subject3) / 3

# Check the grade based on the average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
