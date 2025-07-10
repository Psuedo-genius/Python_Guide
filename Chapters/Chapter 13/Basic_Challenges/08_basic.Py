# Safely try to remove an element that may not exist.
tools = {"pen", "pencil", "apple", "eraser"}
tools.discard("apple")
tools.discard("pineapple")
print(tools)
