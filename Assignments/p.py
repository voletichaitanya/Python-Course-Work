products = {
    1: ["Apple", 30],
    2: ["Banana", 10],
    3: ["Milk", 50],
    4: ["Bread", 25],
    5: ["Eggs", 60],
    6: ["Rice", 70],
    7: ["Sugar", 40],
    8: ["Tea", 120],
    9: ["Coffee", 150],
    10: ["Butter", 90]
}

print("Products available:")
for index, value in products.items():
    print(f"{index}\t{value[0]}\t{value[1]}")

# Take product IDs as input
n = list(map(int, input("\nEnter product IDs (space-separated): ").split()))

# Count quantities
cart = {}
for pid in n:
    cart[pid] = cart.get(pid, 0) + 1

# Print the bill
print("\n" + "="*50)
print("FINAL BILL RECEIPT".center(50))
print("="*50)
print(f"{'Product':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
print("-"*50)

grand_total = 0
for pid, qty in cart.items():
    name, price = products[pid]
    total = price * qty
    grand_total += total
    print(f"{name:<15}{qty:<10}{price:<10}{total:<10}")

print("-"*50)

final_amount = grand_total
print(f"{'Grand Total':<35}{int(final_amount)}")
print("="*50)
print("Thank you for shopping!".center(50))
print("="*50)

