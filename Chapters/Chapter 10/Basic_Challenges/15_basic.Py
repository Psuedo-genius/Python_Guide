# Copy a list and modify the copy without changing the original
fruits = ['apple', 'banana', 'mango', 'grape', 'orange']
fruit = fruits.copy()
fruit.pop(1)
print(fruit)
print(fruits)
