# Encapsulation

class BankAccount:
    # constructor
    def __init__(self, balance):
        self.__balance = balance # The '__' is used to make any variable private. This is the common way to make any variable private in Python


    # functions

    # add money to the bank account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # withdraw money from a bank account
    def withdraw(self, amount):
            self.__balance -= amount


    # get account balance
    def get_balance(self):
        print(f"You have total {self.__balance} euro in your account")

# Creating an object
my_account = BankAccount(1000)
my_account.deposit(2500)
my_account.withdraw(200)
my_account.get_balance()