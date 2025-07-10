# Create a word frequency counter using `.split()`

# Ask for a sentence and split it into words
sentence = input("Enter your sentence: ").split()

# Ask which word to count
word = input("Which word's frequency do you want to check? ")

# Count how many times the word appears
count = sentence.count(word)

# Print the result
print(f"The word '{word}' appears {count} time(s).")
