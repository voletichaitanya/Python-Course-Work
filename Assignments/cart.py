data = {
    1: {'name': 'bananas', 'price': 40},
    2: {'name': 'apples', 'price': 120},
    3: {'name': 'rice', 'price': 60},
    4: {'name': 'sugar', 'price': 45},
    5: {'name': 'corn', 'price': 30},
    6: {'name': 'tomato', 'price': 25},
    7: {'name': 'eggs', 'price': 70},
    8: {'name': 'onions', 'price': 50},
    9: {'name': 'pasta', 'price': 90},
    10: {'name': 'maggie', 'price': 15}
}

# Print table heading
print("Index\tItem\t\tPrice")
print("-" * 30)

# Print each row
for key, item in data.items():
    print(f"{key}\t{item['name']}\t\t₹{item['price']}")
print('-'*30)