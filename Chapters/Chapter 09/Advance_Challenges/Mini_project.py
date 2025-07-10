name = input("Enter name: ").replace(" ", "").lower()
domain = input("Enter domain: ").strip().lower()

email = name + "@" + domain + ".com"
print("Generated email:", email)
