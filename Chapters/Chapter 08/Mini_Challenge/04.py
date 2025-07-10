# Write a loop that keeps printing until user types "stop
while True:
    x = input("Enter something (it will stop on stop)")
    if x == "stop":
        print("Exiting the loop")
        break
'''
Explanation (Line by Line for Beginners):
while True:

    This makes an infinite loop.

    It keeps running forever — until we manually break out using break.

x = input("Enter something...")

    This asks the user to type something.

    Whatever they type is stored in the variable x.

if x == "stop":

    If the user typed the word "stop"...

break

    ...we break out of the loop — stop it completely.

print("Exiting the loop")

    Just a friendly message to say the program is ending.
'''
