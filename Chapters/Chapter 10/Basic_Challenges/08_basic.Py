# Use slicing to get the middle 3 items from a list of 5
fruits = ['apple', 'banana', 'mango', 'grape', 'orange']
print(fruits[1:4])
# OR
for index in range(len(fruits)):
    if index >= 1 and index <= 3:
        print(fruits[index])
