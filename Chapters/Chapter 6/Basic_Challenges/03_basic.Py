# Ask for a number and print if it's + / - / 0
# In this we are chekcing postive negative number
no = int(input("Enter a number: "))
if no > 0:
    print(f"{no} is a positive number.")
elif no < 0:
    print(f"{no} is a negative number.")
else:
    print(f"{no} is zero.")
