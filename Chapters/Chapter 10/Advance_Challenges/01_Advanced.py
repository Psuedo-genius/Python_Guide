# Build a menu where users can add and remove items from a list
menu = ["Idli", "Dosa", "Samosa", "Panipuri"]

while True:
    print("\nCurrent Menu:", menu)

    # Add items
    ask = input("Do you want to add something? (yes/no): ").lower()
    if ask == "yes":
        items = input("Enter dishes to add (space-separated): ").split()
        menu.extend(items)

    # Remove items
    ask = input("Do you want to remove something? (yes/no): ").lower()
    if ask == "yes":
        item_to_remove = input("Enter the dish you want to remove: ")
        if item_to_remove in menu:
            menu.remove(item_to_remove)  # ✅ remove by value, not index
        else:
            print(f"{item_to_remove} is not in the menu.")

    # Optional: exit or continue
    ask = input("Do you want to continue? (yes/no): ").lower()
    if ask == "no":
        break

print("Final Menu:", menu)
