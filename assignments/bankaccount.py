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

acc1 = BankAccount(0.04,50023)
acc2 = BankAccount(0.05, 25330)

acc1.deposit(500).deposit(563).deposit(908).withdraw(776).yield_interest().display_account_info()

acc2.deposit(43).deposit(254).withdraw(500).withdraw(5).withdraw(13).withdraw(776).yield_interest().display_account_info()