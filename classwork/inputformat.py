#String

name = input("Enter your full name: ")

print(name) 

#Integer

item = int(input("Enter the number of items: "))
print(item) 

#Float Input

discount = float(input("Enter the number of discount: "))
print(discount) 

#Input as List (Space-separated)

names = input("Enter employee names (space-separated):").split()
print(names) 


#Input 

tags = input("Enter tags (comma-separated): ").split(',')
print(tags)  


#List 

marks = list(map(int, input("Enter marks: ").split()))
print(marks) 

#List

weights = list(map(float, input("Enter weights: ").split()))
print(weights) 

#Tuple Input

dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
print(dimensions) 

#Set Input

selected_ids = set(map(int, input("Enter selected image IDs:").split()))
print(selected_ids) 

#Dictionary 

profile = eval(input("Enter user profile as a dictionary: "))
print(profile) 

#Multiple Inputs 

username, password = input("Enter username and password:").split()
print("Username:", username)
print("Password:", password)

