'''n = int(input())


for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


n = int(input())


for i in range(n):
    for j in range(2):
        print("*",end=" ")
    print()

n = int(input())


for i in range(n):
    for j in range(n-i-1):
        print("-",end='')
    for j in range(i+1):
        print("*",end='')
    print()

n = int(input())
for i in range(n):
    for j in range(i):
        print("@",end=' ')
    for j in range(n-i):
        print("*",end=' ')
    print()

n = int(input())

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j == n-1 :
            print("*",end='')
        else:
            print(" ",end='')

    print()

#  I
n = int(input())

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or  j==n-j:
            print("*",end='')
        else:
            print(" ",end='')

    print()
'''

