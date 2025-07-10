emails = [
    "john@example.com",
    "amy@example.com",
    "john@example.com",
    "bob@example.com",
    "amy@example.com"
]

unique_emails = set(emails)
clean_list = sorted(unique_emails)

print("Unique emails:")
for email in clean_list:
    print(email)
