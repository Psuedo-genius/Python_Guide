# Print the sum of numbers from 1 to 100 using `while`
# # total = 1+2+3+4+5+6+7+8+9+10+...98+99+100
num = 1
total = 0  # Initialize total to 0
while num <= 100:  # Check if num is less than or equal to 100
    total += num  # Add num to total
    num += 1  # Increment num by 1
print(total, end=' ')
