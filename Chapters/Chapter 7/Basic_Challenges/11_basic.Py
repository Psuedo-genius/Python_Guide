# Print sum of numbers from 1 to 50
# total = 1+2+3+4+5+6+7+8+9+10+...48+49+50
total = 0  # Initialize total to 0
n = int(input('Enter the sum of numbers you want from 1 : '))
# Get input from user
for i in range(1, n+1):
    total += i
print('\nSum of numbers from 1 to 50:', total)
