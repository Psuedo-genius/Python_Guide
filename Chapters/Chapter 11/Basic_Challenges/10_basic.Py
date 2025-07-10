# Combine a tuple and list: `t = (1, [2, 3])` — then change the list
t = (1, [2, 3])        # Tuple with an integer and a list

t[1].append(4)         # Modify the inner list

print(t)               # Output: (1, [2, 3, 4])
