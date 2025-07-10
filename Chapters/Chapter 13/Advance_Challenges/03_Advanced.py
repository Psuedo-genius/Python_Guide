# Filter even numbers from 0–20 using set comprehension.
s = {c for c in range(0, 21) if c % 2 == 0}
print(s)
