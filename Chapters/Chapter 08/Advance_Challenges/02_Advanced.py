# Build a mini calculator (runs until user types "stop")
while True:
    command = input("Enter 'stop' to exit or press Enter to continue: ")
    if command.lower() == "stop":
        print("Calculator exiting... Bye!")
        break

    # Get numbers and operator
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        result = num1 / num2
    else:
        print("Invalid operator!")
        continue

    print(f"Result: {num1} {operator} {num2} = {result}")

# This one was a large code great for understanding.
# Its needs everything you have learned so far.
"""
There one is easier version also but its hard to understand.
# Build a mini calculator (runs until user types "stop")
command = "start"
while command == "start":
    command = input("Enter 'stop' to exit or any other key to continue: ")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    result = eval(f"{num1} {operator} {num2}")
    print(f"Result: {num1} {operator} {num2} = {result}")
    if command == "stop":
        break
"""
# Practice hards kids and always remember to practice!
