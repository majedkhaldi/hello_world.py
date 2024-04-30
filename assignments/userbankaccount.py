class BankAccount:
	def __init__(self, int_rate = 0.01, balance = 0):
		self.int_rate = int_rate
		self.balance = balance 
		
	def deposit(self, amount):
		self.balance += amount
		return self
		
	def withdraw(self, amount):
		self.balance -= amount
		return self
		
	def display_account_info(self):
		print (f"Account: {self.int_rate}, {self.balance}")
		return self
		
	def yield_interest(self):
		self.balance = (self.balance * self.int_rate) + self.balance
		return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.00, balance = 0)

    def make_deposit(self, amount):	
        self.account.balance += amount

    def make_withdrawal(self, amount):
        if self.account.balance > amount:
            self.account.balance -= amount

    def display_balance(self):
        print (f"User: {self.name}, {self.account.balance}")

    def transfer_money(self, other_user, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            other_user.balance += amount
            print(f"Transfer of {amount} to {other_user.name} successful.")
        else:
            print("Insufficient funds for transfer.")
