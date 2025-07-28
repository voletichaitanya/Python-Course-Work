# CONTROL STATEMENTS IN PYTHON

# FOR LOOP EXAMPLE

# Real-Time Scenario: Checking Daily App Usage (Workout Streaks)

workout_log = [1, 1, 1, 0, 1, 1, 0]  # 1 = workout done, 0 = missed
current_streak = 0
longest_streak = 0

for day in workout_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0  # streak breaks

print("Longest workout streak:", longest_streak)

# STRING CHARACTER SEARCH

s = "chaitanya rasool varun tarit sriram praveen".lower()

n = len(s)
c = input("Enter a character to search: ").lower()

for i in range(n):
    if s[i] == c:
        print(f"Character '{c}' found at index {i}")

# PRODUCT AVAILABILITY CHECK

products = ['cycle', 'watch', 'laptop', 'mouse', 'mobile']
items = input("Enter the items to check (space-separated): ").split()

for i in items:
    if i in products:
        print(f"{i} is available at index {products.index(i)}")
    else:
        print(f"{i} is not available")

# WHILE LOOP EXAMPLE
# Real-Time Scenario: Limiting Login Attempts

correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Login successful!")
        break
    else:
        print("Incorrect PIN. Try again.")
        attempts += 1
else:
    print("Account locked due to too many failed attempts.")
