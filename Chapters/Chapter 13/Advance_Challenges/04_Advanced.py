# Compare three sets and find common items using `&`.
day1 = {'Alice', 'Bob', 'Charlie', 'David'}
day2 = {'Bob', 'Charlie', 'Eva'}
day3 = {'Charlie', 'Bob', 'George'}

# Use set intersection (&) to find common students
common_students = day1 & day2 & day3

print("Students present on all three days:")
print(common_students)
