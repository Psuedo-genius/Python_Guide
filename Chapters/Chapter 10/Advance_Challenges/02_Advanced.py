# Take a list of scores, remove the lowest, and print the average
# Step 1: Take space-separated input, convert to integers
scores = list(map(int, input("Enter the marks with space: ").split()))

# Step 2: Sort the scores in ascending order
scores.sort()

# Step 3: Remove the lowest score (first one after sorting)
scores.pop(0)

# Step 4: Calculate the average of remaining scores
average = sum(scores) / len(scores)

# Step 5: Print results
print("Scores after removing lowest:", scores)
print("Average of remaining scores:", average)
