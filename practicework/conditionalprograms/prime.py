num = int(input())

if num <= 1:
    print()
elif num == 2 or num == 3 or num == 5 or num == 7:
    print("Prime number")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("Not a prime number")
else:
    print("Prime number")
