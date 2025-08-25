import my_programs

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Armstrong Number")
        print("2. Swap Two Numbers")
        print("3. Count Vowels in String")
        print("4. GCD of Two Numbers")
        print("5. Reverse a Number")
        print("6. Sum of Digits")
        print("7. Count Words in Sentence")
        print("8. Convert String to Title Case")
        print("9. Factorial of a Number")
        print("10. Fibonacci Series")
        print("11. Palindrome Check")
        print("12. Prime Number Check")
        print("13. Sort a List")
        print("14. Largest of Three Numbers")
        print("15. Convert Decimal to Binary")
        print("0. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting... Goodbye!")
            break
        elif choice == "1":
            my_programs.armstrong_number()
        elif choice == "2":
            my_programs.swap_numbers()
        elif choice == "3":
            my_programs.count_vowels()
        elif choice == "4":
            my_programs.gcd_numbers()
        elif choice == "5":
            my_programs.reverse_number()
        elif choice == "6":
            my_programs.sum_of_digits()
        elif choice == "7":
            my_programs.count_words()
        elif choice == "8":
            my_programs.title_case()
        elif choice == "9":
            my_programs.factorial_number()
        elif choice == "10":
            my_programs.fibonacci_series()
        elif choice == "11":
            my_programs.palindrome_check()
        elif choice == "12":
            my_programs.prime_check()
        elif choice == "13":
            my_programs.sort_list()
        elif choice == "14":
            my_programs.largest_three()
        elif choice == "15":
            my_programs.decimal_to_binary()
        else:
            print("Invalid choice! Please enter a number between 0-15.")

if __name__ == "__main__":
    menu()
