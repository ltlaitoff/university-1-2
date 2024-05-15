import uuid
from .Core import Core

class Manager:
	__core = Core()

	def __init__(self, name, login, password):
		self.id = str(uuid.uuid4())[:5]
		self.name = name
		self.login = login
		self.password = password

	def authorize(self, login, password):
		return self.login == login and self.password == password

	def createNewClient(self, name, login, password):
		return self.__core.createNewClient(self.id, name, login, password)
	
	def showAllClients(self):
		return self.__core.showAllClients(self.id)

	def showAllBankAccounts(self):
		return self.__core.showAllBankAccounts(self.id)

	def showAllBankAccountsByClient(self, clientId):
		return self.__core.showAllBankAccountsByClient(clientId)

	def createNewBankAccount(self, clientId):
		return self.__core.create(self.id, clientId)
	
	def showBankAccountHistory(self, clientId, bankAccountId):
		return self.__core.showHistory(clientId, bankAccountId)
	
	def showBankAccountBalace(self, clientId, bankAccountId):
		return self.__core.showBalance(clientId, bankAccountId)

	def replenishment(self, clientId, bankAccountId, money):
		return self.__core.replenishment(self.id, clientId, bankAccountId, money)
	
	def deleteBankAccount(self, clientId, bankAccountId):
		return self.__core.delete(self.id, clientId, bankAccountId)
	
	def __str__(self) -> str:
		return f"Manager {self.id} | {self.name}"	