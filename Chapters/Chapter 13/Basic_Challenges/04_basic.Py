# Check if a value exists in a set

tools = {"pen", "pencil", "apple", "eraser"}
value = input("value you wanna check")
if value in tools:
    print(f"{value} exist in the set.")
else:
    print(f"{value} doesnt exist in the set")
