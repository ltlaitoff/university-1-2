import uuid
from .Core import Core

class Client:
	__core = Core()

	def __init__(self, name, login, password):
		self.id = str(uuid.uuid4())[:5]
		self.name = name
		self.login = login
		self.password = password

	def authorize(self, login, password):
		return self.login == login and self.password == password

	def showMyBankAccounts(self):
		return self.__core.showAllBankAccountsByClient(self.id)
	
	def showBankAccountHistory(self, bankAccountId):
		return self.__core.showHistory(self.id, bankAccountId)
	
	def showBankAccountBalace(self, bankAccountId):
		return self.__core.showBalance(self.id, bankAccountId)
	
	def widhdrawMoneyFromBankAccount(self, bankAccountId, money):
		return self.__core.widhdraw(self.id, bankAccountId, money)

	def __str__(self) -> str:
		return f"Client {self.id} | {self.name}"	