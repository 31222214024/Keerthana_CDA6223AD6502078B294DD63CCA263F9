# Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 



class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance =initial_balance
    def deposit(self, amount):
      if amount >0:
        self.__account_balance += amount
        print("deposited ₹ {}.New Balance: ₹{}".format(amount, self.__account_balance))
      else:
        print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount>0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("withdraw ₹{}.New balance:₹{}". format (amount,self.__account_balance))
        else:
            print("Insufficient funds")
    def display_balance(self):
        print("Account balance for {}  (Account #{} ):₹{}" .format(self.__account_holder_name, self.__account_number,self.__account_balance))
# Create an instance of the BankAccount class
account = BankAccount(account_number="1234567890", account_holder_name="keerthana",initial_balance= 5000)
# Test the deposit and withdrawal functionality
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.display_balance()
