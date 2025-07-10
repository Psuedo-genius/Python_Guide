# Ask for temperature and classify as cold/warm/hot
temp = int(input("The temperature in celcius"))
if temp < 12:
    print("The temperature is cold")
elif temp < 27:
    print("The temperature is warm")
else:
    print("The temperature is hot")
