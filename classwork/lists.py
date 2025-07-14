#  Creating Lists
l = ['hi', 1, 'helo']  # using []
a = list(['hii', 'hello', 'think'])  # using list() constructor
b = [['hi', 'hel'], [1, 2, 3], ['key', 11]]  # nested lists
d = [11, 5, 3, 55, 6, 8, 77, 98]

#  Basic List Operations
a.append("how")           # append element
print("After append:", a)

print("Pop element:", a.pop())       # removes last
a.sort()                             # sort ascending
print("Sorted list:", a)

a.sort(reverse=True)                # sort descending
print("Reverse sorted list:", a)

print("Element at index 1:", a[1])   # indexing
print("Last element:", a[-1])        # negative index
print("First element:", a[0])

#  Slicing
print("Full reverse:", a[::-1])
print("First two elements:", a[:2])
print("From index 1 to end:", a[1:])

#  Modifying List
a[2] = "hell"
print("Modified element at index 2:", a[2])

a.append(1)           # add duplicate element
a.insert(10, 3)       # insert at position
a.remove(1)           # remove first occurrence of 1
print("After insert & remove:", a)

a.pop()               # remove last
a.clear()             # clear all
print("List after clear:", a)

#  Looping Through a List
fruits = ['apple', 'banana', 'pine', 'grape', 'guava', 'avacado', 'papaya']

print("Loop with for:")
for i in fruits:
    print(i)

fruits.sort(reverse=True)  # sort in descending
print("Reverse sorted fruits:", fruits)

# Indexing & Slicing Examples
my_list = ["Python", "Java", "C++"]
print(my_list[0])  # Python
print(my_list[1])  # Java
print(my_list[-1]) # C++

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30]
print(numbers[2:])      # [30, 40, 50]
print(numbers[-3:-1])   # [30, 40]
print(numbers[::-1])    # reverse list

#  Add Elements
numbers.append(50)
numbers.insert(1, 15)
numbers.extend([60, 70, 80])
print("Numbers after additions:", numbers)

#  Remove Elements
numbers.remove(100)        # try-catch advised
numbers.pop(2)
numbers.pop()
del numbers[1]
numbers.clear()
print("After all removals:", numbers)

#  List Methods Examples
numbers = [3, 1, 4, 1, 5, 9]
print("Count of 1:", numbers.count(1))
print("Index of 4:", numbers.index(4))
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# While loop
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print("While loop:", fruits[i])
    i += 1

# Enumerate loop
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Copying a list
list1 = [1, 2, 3]
list2 = list1.copy()
print("Copied list:", list2)

#  Sorting
numbers = [5, 3, 8, 2]
numbers.sort()
print("Ascending sort:", numbers)

numbers.sort(reverse=True)
print("Descending sort:", numbers)

numbers.reverse()
print("Reversed again:", numbers)
