# Print only even-indexed letters of a string using `enumerate()`.
string = input("Enter something.")

for i, val in enumerate(string):
    if i % 2 == 0:
        print(i, val)
