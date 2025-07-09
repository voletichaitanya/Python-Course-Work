# taking input 
a = input()
print(a)

# integer input
b = int(input())
print(b)

# float input
c = float(input())
print(c)

# default input takes string as input
d = str(input())
print(d)

# list as an input
e = list(map(int,input("".split())))
print(e)

# float of list
j = list(map(float,input("".split())))
print(j)

# set as an input
f = set(map(int,input().split()))
print(f)

# float of set
k = set(map(float,input().split()))
print(k)


# tuple as an input
g = tuple(map(int,input().split()))
print(g)

# dictionary as an input
h = eval(input())
print(h)

# takes anything as an input
i = eval(input())
print(i)