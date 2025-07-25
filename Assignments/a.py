
'''n = input()

p= len(n)

if p==4 or p== 6 and n.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN")'''

n = int(input())

data = {}

for _ in range(n):
    name = input()
    weight = int(input("in kg"))
    height = float(input("in meters"))
    bmi = round(weight /(height ** 2),2)
    data[name]=[bmi]

for name , bmi in data.items():
    print(f'{name} , {bmi}')