"""
Temp ranges:
- <0: "Freezing"
- 0–15: "Cold"
- 16–25: "Cool"
- 26+: "Warm"
"""
temp = float(input("Enter the temperature: "))

if temp < 0:
    print("Temperature is Freezing")
elif temp <= 15:
    print("Temperature is Cold")
elif temp <= 25:
    print("Temperature is Cool")
else:
    print("Temperature is Warm")
