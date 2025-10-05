# Bank Account System

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"{self.account_holder}'s balance: ₹{self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.04):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.account_holder} earned ₹{interest:.2f} interest. New balance: ₹{self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee=50):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total = amount + self.transaction_fee
        if total <= self.balance:
            self.balance -= total
            print(f"{self.account_holder} withdrew ₹{amount} with ₹{self.transaction_fee} fee. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance for withdrawal and fee.")


if __name__ == "__main__":

    savings = SavingsAccount("Gautham", 20000)
    current = CurrentAccount("Neha", 10000)

    
    savings.check_balance()
    savings.deposit(2000)
    savings.apply_interest()
    savings.withdraw(500)

    print()

    
    current.check_balance()
    current.deposit(1000)
    current.withdraw(3000)
    current.withdraw(3500) 

