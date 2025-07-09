# Dictionary creation
student = {
    "name": "chaitanya",
    "age": 21,
    "course": "Computer Science"
}
print(student)

# Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("city", "Not Available"))

# Adding / Updating
student["age"] = 22
student["city"] = "New"
print(student)

# Removing items
student.pop("age")
del student["course"]
student.popitem()
print(student)

student.clear()
print(student)

# Dictionary methods
student = {"name": "chaitanya", "age": 21}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())

student.update({"city": "London"})
print(student)

student.setdefault("gender", "male")
print(student)

# Built-in functions
print(len(student))
print(max({1: "a", 3: "b", 2: "c"}))
print(min({1: "a", 3: "b", 2: "c"}))
print(sorted({3: "x", 1: "y", 2: "z"}))

# Nested dictionary
students = {
    "chaitanya": {"age": 21, "course": "CS"},
    "rasool": {"age": 22, "course": "Math"}
}
print(students["rasool"]["course"])

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)

# Problem 1: Word frequency
sentence = "hello world hello python"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Problem 2: Highest marks
marks = {
    "hell": 85,
    "hii": 92,
    "hey": 88
}
top_student = max(marks, key=marks.get)
print(top_student)
