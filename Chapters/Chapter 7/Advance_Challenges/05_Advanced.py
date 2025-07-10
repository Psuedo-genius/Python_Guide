# Print all prime numbers from 1 to 50 (nested loop logic)
for i in range(2, 51):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
"""
🧠 Now, Line by Line Explanation:
Line 1

for i in range(2, 51):

🔹 This means:

    "Start a loop with a number i that goes from 2 to 50."

    We start at 2 because 1 is not a prime number.

    range(2, 51) means numbers 2 to 50 (51 is not included).

Line 2

    for j in range(2, i):

🔹 This is a nested loop inside the first one.
It means:

    "For each number i, check all numbers j from 2 to i - 1."

We're going to check:

    “Can i be divided evenly by any number smaller than it (except 1)?”

Line 3

        if i % j == 0:

🔹 This checks:

    "If i divided by j leaves no remainder..."
    That means:

    i is divisible by j

    So, i is not a prime number

Line 4

            break

🔹 If the condition above is true:

    "Stop checking — i is not a prime number."

We break out of the inner loop and don’t print anything.
Line 5

    else:

🔹 This else is special — it goes with the for j in range(...) loop.

It means:

    "If the inner loop did not break, then the number is prime."

💡 In other words:

If i was not divisible by any number between 2 and i-1, it’s a prime number!

Line 6

        print(i)

🔹 So we print the number i, because it passed the prime test!
"""
