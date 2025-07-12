s = "chaitanya rasool varun tarit sriram praveen".lower()

n = len(s)
c = input().lower()

for i in range(n) :
    if s[i] == c:
        print(c,i)