year = int(input())

if (year % 400 == 0):
    print(f"{year} is leap and century year")
elif (year % 100 == 0):
    print(f"{year} is century but not leap year")
elif (year % 4 == 0):
    print(f"{year} is leap but not century year")
else:
    print(f"{year} is not leap and not century year")
