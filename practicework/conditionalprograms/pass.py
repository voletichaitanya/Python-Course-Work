password = input()

if len(password)>=8 and password.isalnum :
    print(f"{password} is strong")
else:
    print(f"{password} is not strong")