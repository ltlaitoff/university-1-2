import uuid

class BankAccount:
	def __init__(self, clientId: str):
		self.id = str(uuid.uuid4())[:5]
		self.clientId = clientId
		self.balance = 0
		self.history = []

	def showBalance(self):
		return f"{self.balance}"

	def showHistory(self):
		return f"{self.history}"

	def __str__(self) -> str:
		return f"BankAccount {self.id} | {self.clientId} | {self.balance} | {self.history}"	
