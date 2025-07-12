# Set Basics
s = set()
print(s)  # set()

d = {1, 2, 3}
print(d, type(d))  # {1, 2, 3} <class 'set'>

s = {1, 2, 2, 3, 4}
print(s)  # {1, 2, 3, 4}

# Add & Remove
s.add(5)
s.add(1)
print(s)  # {1, 2, 3, 4, 5}
s.remove(5)
print(s)  # {1, 2, 3, 4}

# Membership
print(3 in s)       # True
print(5 not in s)   # True

# Set Operations
boys = {'rasool', 'varun', 'chaitu', 'tarit'}
girls = {'radha', 'sita', 'gita'}
online = {'praveen', 'tarit', 'madav', 'chaitu'}

print(boys | girls)       # Union
print(boys & girls)       # Intersection
print(boys & online)      # Common
print(boys - online)      # Difference
print(boys ^ girls)       # Symmetric difference

# Subset & Superset
a = {1, 2, 3}
print({1} <= a)           # True
print({1}.issubset(a))    # True
print({1, 2, 3} >= a)      # True
print({1, 2, 3}.issuperset(a))  # True

# Disjoint
print(boys.isdisjoint(girls))   # True
print(boys.isdisjoint(online))  # False

# Built-in Methods
boys.add('fas')
boys.remove('fas')
boys.discard('not_found')
print(boys.pop())         # Random element
boys.clear()
boys.update(('x', 1, 2))
print(boys)

# Update Operations
boys = {'rasool', 'varun', 'chaitu', 'tarit'}
online = {'praveen', 'tarit', 'madav', 'chaitu'}

boys.intersection_update(online)
print(boys)

boys.difference_update(online)
print(boys)

boys.symmetric_difference_update(online)
print(boys)

# Built-in Functions
print(len(boys))
print(min(boys))
print(max(boys))
print(sum({1, 2, 3}))
print(sorted(boys))

# Frozenset
f = frozenset([1, 2, 3])
print(f)
print(len(f), min(f), max(f), sum(f), sorted(f))
