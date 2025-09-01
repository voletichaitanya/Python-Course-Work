# Lambda Functions
#1.Filtering even numbers
n=eval(input())
var = list(filter(lambda x :x%2==0,n))
print(var)
#2 Square lambda function
n = int(input())  # takes an integer input from the user
square_lambda = lambda n: n * n  # defines an anonymous (lambda) function
print('square:', square_lambda(n))  # calls the lambda function and prints the square

#3. Addition
n=int(input())
m=int(input())
add = lambda a,b:a+b
print(add(n,m))

#4.Square lambda
l = [1,2,3,4,5]
square_lambda = list(map(lambda i : i**2 , l))
print('squre:',square_lambda)
n=int(input("Enter the number: "))
l=[i*i for i in range(n)]
print(l)

n=int(input("Enter the number: "))
l=[i for i in range(n) if i%2==0]
print(l)
#5. Upper using lambda
names = ["alice", "bob", "charlie"]
u=[i.upper() for  i in names]
print(u)