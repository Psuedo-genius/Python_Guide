# Ask for time. If <12 → "Good morning"
time = int(input("What hour it is? : "))
if time < 12 and time >= 6:
    print("Good morning")
elif time > 24:
    print("Are you stupid ???")
else:
    print("Why are you late????")
