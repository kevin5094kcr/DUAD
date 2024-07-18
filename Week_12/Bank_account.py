class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount 
            print(f"Withdrew {amount}. New balance {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Cannot witdraw: balance would drop below minimun balance.")

        else:
            super().withdraw(amount)


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)

savings = SavingsAccount(200, 50)
savings.deposit(100)
savings.withdraw(200)
savings.withdraw(300)