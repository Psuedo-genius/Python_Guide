# Merge two user profiles safely.
# 🎯 Goal:
"""user1 = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
user2 = {'email': 'alice.new@example.com', 'city': 'New York'}
merged = {
  'name': 'Alice',
  'email': 'alice.new@example.com',  # user2's value overwrites user1
  'age': 25,
  'city': 'New York'
}"""
'''
✅ Step-by-step:
Input: Two dictionaries — user1 and user2.

Copy user1 to a new dictionary (to avoid modifying the original).

Update the new dictionary with user2.

If a key exists in both → user2's value overwrites user1's.

If a key is only in user2 → it's added.

Return or print the merged dictionary.
'''
user1 = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
user2 = {'email': 'alice.new@example.com', 'city': 'New York'}
merged = user1.copy()
merged.update(user2)
print(merged)
