class Student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.count += 1
    def display(self):
        return f'Name : {self.name} Age : {self.age}'
    @classmethod
    def get_total_students(cls):
        return f"Total students : {Student.count}"

    @staticmethod
    def is_eligible(student):
        if 18 <= student.age <= 30 :
            return True
        else:
            return False

s1 = Student("Alice", 22)   # creates a Student, count = 1
s2 = Student("Bob", 19)     # creates another Student, count = 2
s3 = Student("Shankar",12)

print(s1.display())         # "Name: Alice, Age: 22"
print(s2.display())         # "Name: Bob, Age: 19"
print(s3.display())

print(Student.get_total_students())  # "Total Students: 2"
print(Student.is_eligible(s1))  
print(Student.is_eligible(s2))  
print(Student.is_eligible(s3)) 