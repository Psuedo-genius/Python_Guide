# Count word frequencies from a string using dictionary.
"""
 Algorithm (Step-by-Step Plan)
Take the input string.

Split it into individual words (e.g., using .split()).

Create an empty dictionary to store word counts.

Loop through each word:

If it's already in the dictionary, increase the count.

If not, add it with count 1.

Print the dictionary.
"""
string = input("Enter your sentence: ").split()
dictionary = {}
for word in string:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print(dictionary)
