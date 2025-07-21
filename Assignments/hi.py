'''
#Z
n = int(input())

for row in range(n):
    for col in range(n):
        if row == col  or row+col==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
#X
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j==n-1 :
            print('*',end='')
        else:
            print(' ',end='')
    print()
# I
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j ==n//2:
            print('*',end='')
        else:
            print(' ',end = '')
    print()
# H

n = int(input())
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i ==n//2:
            print('*',end='')
        else:
            print(' ',end = '')
    print()

'''

