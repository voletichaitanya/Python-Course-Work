# my_programs.py

def armstrong_number():
    print("Program: Armstrong Number")
    print("""
def is_armstrong(num):
    s = str(num)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return num == total
""")
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: Check if sum of powered digits equals the number.")


def swap_numbers():
    print("Program: Swap Two Numbers")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(5, -1) -> (-1, 5)")
    print("Explanation: Uses tuple unpacking to swap values.")


def count_vowels():
    print("Program: Count Vowels")
    print("""
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in text if ch in vowels)
""")
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('sky') -> 0")
    print("Explanation: Counts vowels in the string.")


def gcd_numbers():
    print("Program: GCD of Two Numbers")
    print("""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""")
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(7, 5) -> 1")
    print("Explanation: Uses Euclidean algorithm.")


def reverse_number():
    print("Program: Reverse a Number")
    print("""
def reverse_num(n):
    return int(str(n)[::-1])
""")
    print("Test Case 1: reverse_num(1234) -> 4321")
    print("Test Case 2: reverse_num(100) -> 1")
    print("Explanation: Converts to string and reverses.")


def sum_of_digits():
    print("Program: Sum of Digits")
    print("""
def sum_digits(n):
    return sum(int(d) for d in str(n))
""")
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(987) -> 24")
    print("Explanation: Adds digits of number.")


def count_words():
    print("Program: Count Words")
    print("""
def count_words(sentence):
    return len(sentence.split())
""")
    print("Test Case 1: count_words('I love Python') -> 3")
    print("Test Case 2: count_words('Hello') -> 1")
    print("Explanation: Uses split() to count words.")


def title_case():
    print("Program: Title Case")
    print("""
def to_title_case(text):
    return text.title()
""")
    print("Test Case 1: to_title_case('hello world') -> 'Hello World'")
    print("Test Case 2: to_title_case('python programming') -> 'Python Programming'")
    print("Explanation: Uses title() function.")


def factorial_number():
    print("Program: Factorial")
    print("""
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
""")
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Multiply numbers from 1 to n.")


def fibonacci_series():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
""")
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(1) -> [0]")
    print("Explanation: Each term is sum of previous two.")


def palindrome_check():
    print("Program: Palindrome Check")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Compares string with its reverse.")


def prime_check():
    print("Program: Prime Number Check")
    print("""
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
""")
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(9) -> False")
    print("Explanation: Checks divisibility up to sqrt(n).")


def sort_list():
    print("Program: Sort a List")
    print("""
def sort_list(lst):
    return sorted(lst)
""")
    print("Test Case 1: sort_list([3,1,2]) -> [1,2,3]")
    print("Test Case 2: sort_list([5,4,6]) -> [4,5,6]")
    print("Explanation: Uses sorted() to sort list.")


def largest_three():
    print("Program: Largest of Three Numbers")
    print("""
def largest(a, b, c):
    return max(a, b, c)
""")
    print("Test Case 1: largest(10, 20, 15) -> 20")
    print("Test Case 2: largest(-5, -1, -10) -> -1")
    print("Explanation: Uses max() to find largest.")


def decimal_to_binary():
    print("Program: Decimal to Binary")
    print("""
def dec_to_bin(n):
    return bin(n).replace("0b", "")
""")
    print("Test Case 1: dec_to_bin(5) -> '101'")
    print("Test Case 2: dec_to_bin(10) -> '1010'")
    print("Explanation: Uses bin() function to convert.")
