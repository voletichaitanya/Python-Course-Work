class Instagram:
    def __init__(self, username, password):
        print("Welcome to the Instagram")
        self.bio=''
        self.posts=[]
        self.followers={}
        self.following={}
        self.username=username
        self.password=password
        print(f'Hello {self.username} login successful')

mani = Instagram('manikanta','mani@123')


# Example: Understanding self in Python

class Student:
    # Constructor
    def __init__(self, name, age):
        # 'self' refers to the current object being created
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        # Using self to access object properties
        print(f"My name is {self.name} and I am {self.age} years old.")

    # Another method to update age
    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'s age has been updated to {self.age}")

# Creating objects
student1 = Student("Chaitu", 22)
student2 = Student("Teja", 21)

# Each object has its own 'self'
student1.introduce()
student2.introduce()

# Updating student1's age
student1.update_age(23)
student1.introduce()
