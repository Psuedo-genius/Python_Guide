# When does the `else` part of a `for` loop execute?
"""
- When the loop completes successfully (ie, no break statement is encountered).
The `else` part of a `for` loop executes when the loop completes successfully,
meaning it does not execute when a `break` statement is encountered.
This is because a `break` statement immediately exits the loop,
and the `else` clause is executed only after the loop has finished executing.
The `else` clause is useful for performing cleanup tasks or printing a final
message when the loop completes."""

# Example usage
for i in range(5):
    if i == 4:
        break  # Exit the loop early
    # if we remove this line, the else clause will  be executed.
    print(i)
else:
    print("The loop has completed successfully.")
