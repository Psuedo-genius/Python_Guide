# Loop from 1 to 10, but skip 6 and 8
for i in range(1, 11):
    if i == 6 or i == 8:
        continue
    print(i)
