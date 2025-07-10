# Simulate traffic light: red → stop, green → go, yellow → wait
light = input("Enter the traffic light color (red, green, yellow): ")
if light == "red":
    print("Stop!")
elif light == "green":
    print("Go!")
elif light == "yellow":
    print("Wait!")
else:
    print("Invalid color. Please enter either red, green, or yellow.")
