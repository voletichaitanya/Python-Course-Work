# BOOK store

# Taking input

b_id = int(input("Enter Book ID: "))           #  book ID
title = input("Enter Book Name: ")             # book title
price = float(input("Enter Book Price: "))     # book price

# categories list

cats = input("Enter Categories (comma-separated): ").split(',')

# tuple (available, sold)

avail = int(input("Enter Available Stock: "))
sold = int(input("Enter Sold Stock: "))
stock_info = (avail, sold)

# discount as float

disc = float(input("Enter Discount Percentage: "))

# features as set

feats = set(input("Enter Book Features (comma-separated): ").split(','))

# Printing the details

print("\n--- Book Details ---")

# 1. Using comma separator

print("Book ID, Name, Price:", b_id, title, price, sep=", ")

# 2. Using % formatting

print("Discount: %.2f%%" % disc)

# 3. Using f-strings

print(f"Name: {title}")
print(f"Price: ₹{price}")
print(f"Stock: {stock_info[0]} available, {stock_info[1]} sold")

# 4. Extra info

print("Categories:", cats)
print("Features:", feats)
