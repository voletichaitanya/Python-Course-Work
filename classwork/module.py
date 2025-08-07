'''import sys
print(sys.path)
print(sys.argv)
print(sys.path)
print(sys.exit)

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math

print(math.gcd(34,77))
print(math.log(10))
print(math.sin(30))
print(math.cos(45))
print(math.tan(60))
print(math.degrees(90))
print(math.radians(45))
print(math.factorial(5))
print(math.ceil(2.3))
print(math.floor(30.6))
print(math.pow(3,4))
print(math.sqrt(6))
print(math.fabs(4))


import random
random.seed(10)
print(random.random())
print(random.randint(1,6))
print(random.uniform(5,7))
fruits = ['apple','banana','pine','mango','grapes','papaya']
print(random.choice(fruits))
print(random.choices(fruits,k=2))
random.shuffle(fruits)
print(fruits)

import collections

w='python programming language'
x='python programming python language programming'.split()
d = collections.Counter(w)
e = collections.Counter(x)
print(d)
print(e)


s = 'abcdefghijklmnopqrstuvwxxyz'
d = collections.defaultdict()
for i in range(len(s)):
    d[i+1]=s[i]

print(d)

from collections import deque

l=deque()

l.append(9)
l.appendleft(36)
l.append(66)
l.append(45)
l.pop()
l.append(90)
l.pop()

print(l)



from itertools import permutations,combinations

p = print(list(permutations('abc',2)))
c = print(list(combinations('abc',2)))
'''

from datetime import date , time , datetime , timedelta

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d=date(2025,5,20)
print(d)
t=time(14,59,59)
print(t)

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(f"{now.hour:02}:{now.minute:02}:{now.second:02}")


print(now.strftime('%d %m %y'))
print(now.strftime('%d %b, %Y'))
print(now.strftime('%d %b, %Y  %H : %M : %M'))
print(now.strftime('%d %b, %Y  %H : %M : %M   %p' ))
print(now.strftime('%a %d %b, %Y  %H : %M : %M '))
print(now.strftime('%A %d %b, %Y  %H : %M : %M '))

fdate = today - timedelta(days=7)
ftime = now - timedelta(minutes=30)
print(fdate,ftime)















