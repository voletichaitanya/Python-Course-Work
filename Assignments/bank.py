data = {
    12345: {"pin": 123, "balance": 5678, "history": []},
    12346: {"pin": 456, "balance": 9000, "history": []},
    12347: {"pin": 789, "balance": 1200, "history": []},
    12348: {"pin": 321, "balance": 3000, "history": []},
    12349: {"pin": 654, "balance": 7500, "history": []},
}

def welcome():
    print("\n      welcome\n".center(1000,'-'))
def login():
    acc_num=int(input())
    pin=int(input())
    if acc_num in data:
        if data[acc_num]["pin"] == pin:
            print("Login successful!\n")
            return acc_num
        else:
            print("Incorrect PIN!\n")
    else:
        print("Account number not found!\n")

    return None


def check_balance(acc_num, data):
    balance = data[acc_num]["balance"]
    print(f"Your current balance is: ₹{balance}\n")



def credit_money(acc_num, data):
    current_balance = data[acc_num]["balance"]
    print(f"Current Balance: ₹{current_balance}")
    
    amount = float(input("Enter amount to credit: ₹"))
    
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.\n")
        return
    data[acc_num]["balance"] += amount
    data[acc_num]["history"].append(f"Credited ₹{amount}")

    print(f"Amount credited successfully!")
    print(f"Updated Balance: ₹{data[acc_num]['balance']}\n")


def debit_money(acc_num, data):
    current_balance = data[acc_num]["balance"]
    print(f"Current Balance: ₹{current_balance}")
    
    amount = float(input("Enter amount to debit: ₹"))
    
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.\n")
        return

    if amount > current_balance:
        print("Insufficient balance!\n")
        return
    data[acc_num]["balance"] -= amount
    data[acc_num]["history"].append(f"Debited ₹{amount}")

    print("Amount debited successfully!")
    print(f"Updated Balance: ₹{data[acc_num]['balance']}\n")

def view_history(acc_num, data):
    history = data[acc_num]["history"]
    if not history:
        print("No transaction history available.\n")
    else:
        print("Transaction History:")
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")
        print()

