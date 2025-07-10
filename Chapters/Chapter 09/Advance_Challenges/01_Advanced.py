# Build a simple Caesar cipher (shift characters by 1)
"""🧠 Simple Algorithm (Step-by-step)

    Ask user to enter a message (word or sentence).

    Create an empty string to store the ciphered result.

    Loop through each character in the message.

    If the character is:

        a lowercase letter: shift it forward by 1

        a uppercase letter: shift it forward by 1

        anything else (like space or punctuation): keep it as-is

    If the character is "z" or "Z" → wrap around to "a" or "A"

    Add the shifted letter to the result string.

    Print the final encrypted message.
"""
text = input("Enter your message")
cipher = ""
for char in text:
    if text.isalpha:
        if text.islower():
            shifted = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
        else:
            shifted = chr((ord(char) - ord('A') + 4) % 26 + ord('A'))
        cipher += shifted
    else:
        cipher += char  # Keep spaces and punctuation as they are
print("Encrypted message:", cipher)
"""
ord(char) → turns a letter into its number (ASCII code)

chr(num) → turns a number back into a letter

% 26 → makes sure after "z" or "Z" it wraps back to "a" or "A"
"""
"""
🧠 Step-by-Step Breakdown
Say char = 'y'
🔢 Step 1:

ord(char) - ord('a')

    Converts char to its position in alphabet (starting from 0):

    ord('y') = 121, ord('a') = 97

    So: 121 - 97 = 24 → 'y' is the 25th letter (index 24)

➕ Step 2:

(ord(char) - ord('a')) + 1

    We add 1 to shift forward:

    24 + 1 = 25

⏰ Step 3:

% 26

    % 26 ensures that after 'z', we wrap back to 'a'

    For example:

    If char is 'z': ord('z') = 122 → 122 - 97 = 25 → 25 + 1 = 26 → 26 % 26 = 0

    0 = position of 'a'

➕ Step 4:

+ ord('a')

    We turn the shifted alphabet index back into an ASCII code

    So: 25 + 97 = 122 → chr(122) = 'z'

🔁 Final:

chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

    Converts 'y' → 'z'

    Converts 'z' → 'a'
"""
# Hope you understand this one and flex it to your stupid friends.
