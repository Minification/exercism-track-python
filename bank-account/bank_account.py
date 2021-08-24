import threading

class BankAccount:
	def __init__(self) -> None:
		self.__lock__ = threading.Lock()
		with self.__lock__:
			self.is_closed = True
			self.balance = 0

	def get_balance(self):
		with self.__lock__:
			if self.is_closed:
				raise ValueError("Account is closed!")
			return self.balance

	def open(self):
		with self.__lock__:
			if not self.is_closed:
				raise ValueError("Account is already open!")
			self.balance = 0
			self.is_closed = False

	def deposit(self, amount: int):
		if amount < 0:
			raise ValueError("Amount must be nonnegative!")
		with self.__lock__:
			if self.is_closed:
				raise ValueError("Account is closed!")
			self.balance += amount

	def withdraw(self, amount: int):
		if amount < 0:
			raise ValueError("Amount must be nonnegative!")
		with self.__lock__:
			if self.is_closed:
				raise ValueError("Account is closed!")
			if self.balance < amount:
				raise ValueError("Cannot withdraw more than balance!")
			self.balance -= amount

	def close(self):
		with self.__lock__:
			if self.is_closed:
				raise ValueError("Account is already closed!")
			self.is_closed = True
