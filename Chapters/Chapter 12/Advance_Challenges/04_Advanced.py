# Use nested dictionaries to model a product catalog
catalog = {
    'P001': {'name': 'Laptop', 'price': 75000, 'stock': 12},
    'P002': {'name': 'Smartphone', 'price': 25000, 'stock': 30},
    'P003': {'name': 'Headphones', 'price': 3000, 'stock': 50}
}

# Access details of a specific product
product_id = 'P002'
product = catalog.get(product_id)

if product:
    print(f"Product: {product['name']}")
    print(f"Price: ₹{product['price']}")
    print(f"Stock: {product['stock']}")
else:
    print("Product not found.")
