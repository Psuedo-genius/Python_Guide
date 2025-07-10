# Why do we need `x += 1` or similar in a `while` loop?
# Answer: The `while` loop continues running as long as the condition
# (x < 5) is True. If `x += 1` is included in the loop, the value of `x`
#  will increase by 1 each time the loop runs, eventually reaching or
# exceeding 5. This will continue indefinitely until the condition (x < 5)
# is no longer True.
# Insimple words,the loop will keep running until thecondition is no longer met
