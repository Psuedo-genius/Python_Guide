# Show the difference between =  and ==  in a short snippet
s = 'Hello, World!'
print(f"Using the \'=\' {s}")
t = s
t == 'hello, World!'  # Output: True
print(f"Using the \'==\' {t}")
