# Use `zip()` to match countries and capitals.
countries = ["India", "China", "Pakistan"]
capitals = ["New Delhi", "Beijing", "Islamabad"]

# Zip the two lists together
paired = list(zip(countries, capitals))

# Print as list of tuples
print("Zipped pairs:", paired)

# Or loop and print nicely
for country, capital in zip(countries, capitals):
    print(f"{country} ➝ {capital}")
