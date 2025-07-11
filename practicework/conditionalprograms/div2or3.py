num = int(input())

if num%2 == 0  and num%3 ==0 :
    print("divisible by 2 and 3")
elif num%2 == 0 :
    print("divisible by 2")
elif num%3 == 0:
    print("divisible by 3")
else:
    print("Not divisible by 2 and 3")