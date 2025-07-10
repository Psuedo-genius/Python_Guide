# What does this print?
i = 0
while i < 3:
    i += 1
    if i == 2:
        break
else:
    print("Done")
# Expected output: noting sicne 'break' is encountered before the loop ends
