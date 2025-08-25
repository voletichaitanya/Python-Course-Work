prices = [100, 200, 300]
print("Total:", sum(prices))

def greet(name):
    print("Hello", name)

greet("Chaitu")

def order_item(item, quantity, price=50, discount=0):
    total = (price * quantity) - discount
    print("Bill:", total)

order_item("Pen", 2)
order_item("Book", 3, 100)
order_item(item="Bag", quantity=1, price=200, discount=20)

def final_bill(amount, gst):
    return amount + (amount * gst / 100)

print("Final Bill:", final_bill(1000, 18))

def change_voucher(v):
    v = 500
    print("Inside:", v)

def add_item(c):
    c.append("Shoes")
    print("Inside:", c)

voucher = 1000
change_voucher(voucher)
print("Outside:", voucher)

cart = ["Bag"]
add_item(cart)
print("Outside:", cart)

def loyalty_points(p):
    if p == 0:
        return 0
    return 10 + loyalty_points(p-1)

print("Points:", loyalty_points(3))