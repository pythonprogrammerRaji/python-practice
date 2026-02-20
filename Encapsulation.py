        # create a BackAccount class with private attributes for account_number and balance, add method to check
        # balance, deposit, and withdraw funds and tru accessing the balance directly and observe the result

        class BankAccount:
            def __init__(self, account_number, balance):
                self.__account_number = account_number
                self.__balance = balance

            def check_balance(self):
                print(f"{self.__balance}")

            def deposit(self):
                print(f"{self.__account_number}")

            def withdraw(self):
                print("withdraw funds")


        bank = BankAccount("Sbi123", "1000")

        # print(bank.self__balance)
        bank.check_balance()
        bank.deposit()
        bank.withdraw()
