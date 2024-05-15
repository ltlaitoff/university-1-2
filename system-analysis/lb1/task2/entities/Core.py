from typing import List, Union
from typing import TYPE_CHECKING
from .BankAccount import BankAccount

if TYPE_CHECKING:
	from .Client import Client
	from .Manager import Manager

class SingletonMeta(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]


class Core(metaclass=SingletonMeta):
	__ADMIN_PASSWORD = "admin"

	def __init__(self):
		self.clients: List['Client'] = []
		self.managers: List['Manager'] = []
		self.bankAccounts: List['BankAccount'] = []

	def authorizarion(self, accountType, login, password):
		if (accountType == "client"):
			for manager in self.clients:
				if (manager.authorize(login, password)):
					return manager

		if (accountType == "manager"):
			for manager in self.managers:
				if (manager.authorize(login, password)):
					return manager

		return None

	def __checkIfManagerIdValid(self, managerId):
		for manager in self.managers:
			if (manager.id == managerId):
				return manager 

		return False	

	def __checkIfClientdValid(self, clientId):
		for client in self.clients:
			if (client.id == clientId):
				return client

		return False	

	def __checkIfBankAccountIdValid(self, clientId, bankAccountId):
		for bankAccount in self.bankAccounts:
			if (bankAccount.clientId == clientId and bankAccount.id == bankAccountId):
				return bankAccount

		return False	

	def showAllClients(self, managerId):
		if (not self.__checkIfManagerIdValid(managerId)):
			return None

		return self.clients

	def showAllBankAccounts(self, managerId):
		if (not self.__checkIfManagerIdValid(managerId)):
			return None
		
		return self.bankAccounts

	def showAllBankAccountsByClient(self, clientId):
		if (not self.__checkIfClientdValid(clientId)):
			return None
		
		return list(filter(lambda bankAccount: bankAccount.clientId == clientId, self.bankAccounts))

	def create(self, managerId, clientId) -> Union[BankAccount, None]:
		if (not self.__checkIfManagerIdValid(managerId)):
			return None
		
		if (not self.__checkIfClientdValid(clientId)):
			return None
  
		bankAccount = BankAccount(clientId)
		self.bankAccounts.append(bankAccount)

		return bankAccount

	def replenishment(self, managerId, clientId, bankAccountId, money):
		if (not self.__checkIfManagerIdValid(managerId)):
			return None
		
		if (not self.__checkIfClientdValid(clientId)):
			return None

		bankAccount = self.__checkIfBankAccountIdValid(clientId, bankAccountId)

		if (not bankAccount):
			return None

		# TODO: Change to method
		bankAccount.balance += money

		return bankAccount.balance
	
	def delete(self, managerId, clientId, bankAccountId):
		return ""
	
	def showBalance(self, clientId, bankAccountId):
		if (not self.__checkIfClientdValid(clientId)):
			return 'Not found client' 

		bankAccount = self.__checkIfBankAccountIdValid(clientId, bankAccountId)

		if (not bankAccount):
			return 'Not found bank account' 

		return bankAccount.showBalance()	
	
	def showHistory(self, clientId, bankAccountId):
		if (not self.__checkIfClientdValid(clientId)):
			return None

		bankAccount = self.__checkIfBankAccountIdValid(clientId, bankAccountId)

		if (not bankAccount):
			return None

		return bankAccount.showHistory()	

	def widhdraw(self, clientId, bankAccountId, money):
		if (not self.__checkIfClientdValid(clientId)):
			return None

		bankAccount = self.__checkIfBankAccountIdValid(clientId, bankAccountId)

		if (not bankAccount):
			return None

		# TODO: Change to method
		bankAccount.balance -= money

		return (bankAccount.balance, money)

	def createNewClient(self, managerId, name, login, password):
		if (not self.__checkIfManagerIdValid(managerId)):
			return None
		
		from .Client import Client
		client = Client(name, login, password)

		self.clients.append(client)

		return client

	def createNewManager(self, rootAdminToken, name, login, password):
		if (not (rootAdminToken == self.__ADMIN_PASSWORD)):
			return None
		
		from .Manager import Manager
		manager = Manager(name, login, password)

		self.managers.append(manager)

		return manager
	
	def showAll(self, rootAdminToken):
		if (not (rootAdminToken == self.__ADMIN_PASSWORD)):
			return None

		managers = "\n".join([ str(manager) for manager in self.managers])
		clients = "\n".join([ str(client) for client in self.clients])
		bankAccounts = "\n".join([ str(bankAccount) for bankAccount in self.bankAccounts])
		
		return "\n\n".join([managers, clients, bankAccounts])