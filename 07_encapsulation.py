# ==========================================
# Encapsulation in Python
# ==========================================

# Encapsulation is the process of
# hiding data and providing controlled
# access through methods.

# ------------------------------------------
# Class Definition
# ------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder

        # Private Variable
        self.__balance = balance

    # Getter Method
    def get_balance(self):

        return self.__balance

    # Setter Method
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")

    # Withdraw Method
    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Display Account Details
    def display_account(self):

        print("\nAccount Details")
        print("----------------")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : ₹{self.__balance}")


# ------------------------------------------
# Creating Object
# ------------------------------------------

account = BankAccount(
    "Shweta",
    5000
)

# ------------------------------------------
# Operations
# ------------------------------------------

account.display_account()

account.deposit(2000)

account.withdraw(1000)

account.display_account()
