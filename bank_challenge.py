class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0  # protected = encapsulation

    def check_account(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit amount Successfully, the balance is {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw amount Successfully, the balance is {self._balance}")
        else:
            print("Not sufficient amount in account")


class SavingAccount(Account):  #intertance
    def calculate_interest(self):
        INTERES_RATE = 0.04 # 4%
        interest = self._balance * INTERES_RATE
        print(f"The interest is {interest}" )

class CurrentAccount(Account):
    def overdraft(self,amount):
        OVER_DRAFT = 1000
        if self._balance + OVER_DRAFT >= amount:
            self._balance -= amount
            print(f"Withdraw amount Successfully, the balance is {self._balance}")
        else:
            print("sufficient amount in account")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}
    def create_account(self, id, holder_name, type):
        if type =="savings":
            new_account = SavingAccount(id, holder_name)
        elif type=="current":
            new_account = CurrentAccount(id,holder_name)
            







