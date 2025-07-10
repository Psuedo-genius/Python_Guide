# Check if a student exists in the dictionary.
mydi = {'Rahul': 98, 'Divya': 78, 'Sonam': 90, 'Jack': 78}
name = input("Name you wanna check")
print(mydi.get(name, "Not found"))

# or but since hint says use "in" this one is correct
name = input("Name you wanna check: ").strip().lower()
found = False
for k in mydi:
    if k.lower() == name:
        print(mydi[k])
        found = True
        break
if not found:
    print("Not found")
