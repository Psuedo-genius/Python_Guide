# Build a whitelist + blacklist filter using sets and set difference
whitelist = {'Alice', 'Bob', 'Charlie', 'David'}
blacklist = {'Charlie', 'Eva', 'Frank'}

# Allow only users who are in whitelist and NOT in blacklist
filtered_users = whitelist - blacklist

print("Allowed users:")
print(filtered_users)
