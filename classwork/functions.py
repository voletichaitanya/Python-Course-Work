#builtin functions
print(len("Hello")) # Output: 5
print(abs(-10)) # Output: 10

#User defined functions
def add(a, b):
    #This function adds two numbers."""
    return a + b

print(add(5, 10)) # Output: 15


#functional arguments and types ....
#1.positional argu
data=('xyz@gmail.com','xyz@123')
def login(mail,username,password):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(mail,username,password)

#2.keyword arg
data=('xyz@gmail.com','xyz@123')
def login(mail,user,passw):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(username=username,mail=mail,password=password)

#3.default arg
data=('xyz@gmail.com','xyz@123')
def login(username, password, mail='xyz@gmail.com'):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(username,password)

#4.Variable-Length Arguments
#'*args' (Arbitrary Positional Arguments)
def add(*numbers):
    return numbers
print(add(1, 2, 3, 4, 5))#(1, 2, 3, 4, 5)


# 5. '**kwargs' (Arbitrary Keyword Arguments)
def display(**l):
    return l
print(display(py=289,spl=12123,htm=123))#{'py': 289, 'spl': 12123, 'htm': 123}
print(display(py=2,spl=3212,htm=13))#{'py': 2, 'spl': 3212, 'htm': 13}
print(display(py=12,spl=312,htm=1))#{'py': 12, 'spl': 312, 'htm': 1}

#6.built-in scope
l=[1,2,3,4]
#sum=0 #overriding , not delcare them cause they are already a global scope
print(sum(l))  #10

#7.Recursive Functions

def numbers(n):
    if n==0:
        return n
    return n+(numbers(n-1))

n = int(input())
print(numbers(n))

#8.Recursive product function

def product(n):
    if n==1:
        return 1
    return n * product(n-1)

n=int(input())
print(product(n))

#9. Recursive Traversal function

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='')
    display(s,ind+1)

s = input()
print(display(s,0))

#10.function recursive sum of digits

def sumofdigit(n):
    if n<=0:
        return n
    return (n%10)+sumofdigit(n//10)
n=int(input())
print(sumofdigit(n))

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='\t')
    display(s,ind+1)
    print(s[ind],end='\t')
s = input()
print(display(s,0))