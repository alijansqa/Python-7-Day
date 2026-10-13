# Encapsulation
# To hide data
# To make variable private
# by using __

class BankAccout:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
    def get_balance(self):
        return self.balance

account = BankAccout(1000)
account.deposit(1000)
account.withdraw(500)
# hacker comes
account.balance = 100000
print(account.get_balance()) # account balance = 100000. this is why we hide variable by adding __


# Encapsulation

class BankAccout:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance

account = BankAccout(1000)
account.deposit(1000)
account.withdraw(500)
# hacker comes
account.balance = 100000  # will not work or be accessed
print(account.get_balance())





# Default Encapsulation by self.balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc


    def withdraw(self, amount):
        self.balance -= amount
        print("Rs.", amount, "Withdrawn")
        print("Total Balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "Credited")
        print("Total Balance=", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000000000, 10001)
acc1.withdraw(50000)
acc1.credit(1000000)
