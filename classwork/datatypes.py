# Python Data Types Demo

# Integer
a = int(23)
b = 23
print("Integer values:", a, b)
print("Type of a:", type(a))
print("Type of b:", type(b))

# Float
c = 2.3
d = float(2.3)
print("\nFloat values:", c, d)
print("Type of c:", type(c))
print("Type of d:", type(d))

# Complex Number
f = 2 + 3j
print("\nComplex value:", f)
print("Type of f:", type(f))

# String
g = 'hai'
print("\nString value:", g)
print("Type of g:", type(g))

# List
l = list()
i = [1, 2, 3, 4, 5]
print("\nList values:", i, l)
print("Type of i:", type(i))
print("Type of l:", type(l))

# Tuple
t = tuple()
o = (1, 2, 3)
print("\nTuple values:", t, o)
print("Type of t:", type(t))
print("Type of o:", type(o))

# Set
s = set()
k = {1, 2, 3, 3, 4, 'c', 23.45, "d"}  # duplicates are automatically removed
print("\nEmpty set:", s)
print("Set with elements:", k)
print("Type of k:", type(k))

# Dictionary
u = dict()
v = {'name': "Rasool", 'age': 12}
print("\nEmpty dictionary:", u)
print("Dictionary with values:", v)
print("Type of v:", type(v))
print("Type of u:", type(u))

# Boolean
t = True
f = False
print("\nBoolean values:", t, f)
print("Type of t:", type(t))
print("Type of f:", type(f))

# NoneType
d = None
print("\nNone value:", d)
print("Type of d:", type(d))

# Summary with alternate definitions
print("\n--- Summary Examples ---")
a = 10
print(a, "->", type(a))   # int

b = 10.0
print(b, "->", type(b))   # float

c = "Chaitanya"
print(c, "->", type(c))   # str

d = list([1, 2, 3])
print(d, "->", type(d))   # list

e = set(["i", "t", "g"])
print(e, "->", type(e))   # set

f = tuple([1, 3, 2, 5, 7])
print(f, "->", type(f))   # tuple

g = {"name": "Chaitanya", "reg": "12"}
print(g, "->", type(g))   # dict

h = None
print(h, "->", type(h))   # NoneType

i = 1 + 9j
print(i, "->", type(i))   # complex
