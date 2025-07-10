# Remove all vowels from a string
"""
🧠 Algorithm: Remove Vowels from a String
Step-by-Step:

    Start

    Ask the user to enter a string (could be a sentence).

    Define a list or string of vowels: a, e, i, o, u

    Create an empty string new_para to store result without vowels

    Loop through each character in the input string:

        If the character is not a vowel (use .lower() to handle uppercase):

            Add the character to new_para

    After the loop ends, print new_para — this is the version without vowels

    End
"""
para = input("Enter the string: ").lower()
vowels = ["a", "e", "i", "o", "u"]
new_para = ""
for char in para:
    if char not in vowels:
        new_para += char
print("The vowels free sentence is:", new_para)
