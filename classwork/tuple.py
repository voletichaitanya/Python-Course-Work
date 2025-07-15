# Day 7 — Python Tuples

# Tuple Creation
t1 = ()                              # Empty tuple
t2 = (5,)                            # Single-element tuple (note the comma)
t3 = (1, "apple", 3.5)               # Mixed data types
t4 = 1, 2, 3                         # Tuple without parentheses
print(t1, t2, t3, t4)

# Indexing & Slicing
t = (10, 20, 30, 40, 50)
print(t[2])                          # Accessing by index
print(t[-1])                         # Negative indexing
print(t[1:4])                        # Slicing

# Tuple Operations
a = (1, 2)
b = (3, 4)
print(a + b)                         # Concatenation
print(a * 3)                         # Repetition
print(2 in a)                        # Membership test
print(5 not in a)

# Tuple Unpacking
x, y, z = (1, 2, 3)
print(x, y, z)

# Tuple Methods
t = (1, 2, 2, 3)
print(t.count(2))                    # Count occurrences
print(t.index(3))                    # Index of value

# Built-in Functions
n = (5, 10, 15)
print(len(n))                        # Length
print(max(n))                        # Max value
print(min(n))                        # Min value
print(sum(n))                        # Sum
print(tuple([4, 5, 6]))              # Convert list to tuple

# Tuple Immutability with Mutable Elements
nested = (1, [2, 3])
nested[1][0] = 100                   # Allowed: list inside tuple is mutable
print(nested)

# Tuple as Dictionary Key
d = {(1, 2): "yes"}
print(d[(1, 2)])

# Function Returning Tuple
def get_vals():
    return (10, 20)
a, b = get_vals()
print(a, b)

# Conversion
print(list((1, 2, 3)))              # Tuple to list
print(tuple([7, 8, 9]))             # List to tuple
