# Print multiplication table of 7
no = int(input("Enter the number table you want"))
for i in range(no, no+1):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*(j)}',)
    print()
