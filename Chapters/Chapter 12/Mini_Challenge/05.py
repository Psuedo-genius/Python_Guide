# Use dict comprehension to square numbers 1–5.
dic = {x: x*x for x in range(1, 6)}

for key, value in dic.items():
    print(f"{key}: {value}")
