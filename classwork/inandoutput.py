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
a , b , c = 10,20,30
print(a,b,c)
print("%d %d %d"%(a,b,c))
print(f'a={a} , b = {b} , c = {c}')
print("hello","banana","grapes" , end = "_")
print("hello",end = " ")
print("how are you")
print("hii","hey","how","are","you" , sep = "   ")
print("line 1 \n line 2")
name = "Diana"
age = 22
score = 89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,
score))
