# If condition

num = int(input())

if num > 18 :
    print("Can vote !")


# If Else Condition

ag  = int(input())

if ag > 18 :
    print("Can vote !")
else:
    print("Can not vote !")


# If Else If Condition 

temp = int(input())

if temp <15 :
    print("Cold")
elif temp>15 and temp<30:
    print("Moderate")
else:
    print("Hot")


# Nested If Condition

age = int(input("Enter your age: "))
time = int(input("Enter showtime (in 24hr format, e.g., 16 for 4 PM): "))

if age < 18:
    if time < 17:
        price = 100
    else:
        price = 120
else:
    if time < 17:
        price = 150
    else:
        price = 200

print(f"Your ticket price is ₹{price}")
