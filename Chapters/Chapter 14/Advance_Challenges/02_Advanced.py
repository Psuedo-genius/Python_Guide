#  Write a calculator function using `if`, `elif` inside it.
def calculator(num1, num2, opre):
    if opre == "+":
        return num1 + num2
    elif opre == "-":
        return num1 - num2
    elif opre == "*":
        return num1 * num2
    elif opre == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif opre == "%":
        return num1 % num2
    elif opre == "**":
        return num1 ** num2
    else:
        return "Invalid operator"


# Taking input from the user
num1 = int(input("Enter first number: "))
opre = input("Enter operator (+, -, *, /, %): ")
num2 = int(input("Enter second number: "))

# Call the function and print result
result = calculator(num1, num2, opre)
print("Result:", result)
