# Extract the domain name from an email like "user@gmail.com"
email_id = input("Enter your Email ID: ")
index = email_id.find("@")
if index != -1:
    domain = email_id[index+1:]
    print(f"Your domain name id {domain}")
else:
    print("You don't have domain id.")
