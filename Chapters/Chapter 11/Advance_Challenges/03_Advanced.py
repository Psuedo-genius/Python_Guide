# Given two tuples: one with names and one with scores,
# pair them using `zip()` and print results in the format: `Name scored Score`.
t1 = ("Rahul", "Mario", "Genius")
scores = (78, 87, 94)

for name, score in zip(t1, scores):
    print(f"{name} scored {score}")
