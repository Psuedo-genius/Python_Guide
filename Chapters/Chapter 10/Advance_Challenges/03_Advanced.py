# Track a list as a shopping cart (add/remove/view items)
cart = []

while True:
    action = input("Add / Remove / View / Quit: ").lower()

    if action == "add":
        item = input("Item name: ")
        cart.append(item)

    elif action == "remove":
        item = input("Remove what?: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Not found.")

    elif action == "view":
        print("Grocery List:", cart)

    elif action == "quit":
        break
