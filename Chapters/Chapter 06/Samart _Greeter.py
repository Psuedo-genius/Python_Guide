user_name = input("Enter your name: ")
time = int(input("Enter the current time in 24-hour format (e.g., 14): "))
if time < 12:
    greeting = f"Good morning, {user_name}!"
elif time >= 12 and time < 18:
    greeting = f"Good afternoon, {user_name}!"
elif time > 24 or time < 0:
    greeting = "Stupid input! Please enter a valid time between 0 and 24."
else:
    greeting = f"Good evening, {user_name}!"
print(greeting)
