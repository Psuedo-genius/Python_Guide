#  Use symmetric difference to compare student attendance on two days.
day1 = {'Alice', 'Bob', 'Charlie', 'David'}
day2 = {'Charlie', 'Eva', 'Bob', 'Fiona'}

# Symmetric difference: present on only one of the days
only_one_day = day1 ^ day2

print("Students present on only one of the two days:")
print(only_one_day)
