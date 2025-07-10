# Check if `99` is in a given tuple
t = (234, 243, 265, 653, 99)
n = int(input("The NUmber you wanna check in tuple: "))
if n in t:
    print(f"Yes {n} is present in tuple")
else:
    print(f"{n} is not in tuple")
