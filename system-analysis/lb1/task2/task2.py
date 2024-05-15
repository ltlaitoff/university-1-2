from task2.entities.Auhorization import Authorizarion
from task2.entities.Client import Client
from task2.entities.Core import Core
from task2.entities.Manager import Manager

class Task2:
	__ADMIN_PASSWORD = "admin"

	def initializeBaseStructureAsAdmin(self):
		manager1 = Core().createNewManager(self.__ADMIN_PASSWORD, "Manager 1", "m1", "m1")
		manager2 = Core().createNewManager(self.__ADMIN_PASSWORD, "Manager 2", "m2", "m2")

		if (manager1 == None or manager2 == None):
			print("Error in initialize")
			return

		client1 = Core().createNewClient(manager1.id, "Client 1", "c1", "c1")
		client2 = Core().createNewClient(manager1.id, "Client 2", "c2", "c2")
		client3 = Core().createNewClient(manager2.id, "Client 3", "c3", "c3")
		client4 = Core().createNewClient(manager2.id, "Client 4", "c4", "c4")
		client5 = Core().createNewClient(manager2.id, "Client 5", "c5", "c5")
	

		if (not client1 or not client2 or not client3 or not client4 or not client5):
			print("Error in initialize")
			return

		Core().create(manager1.id, client1.id)
		Core().create(manager1.id, client1.id)

		Core().create(manager1.id, client2.id)

		Core().create(manager2.id, client3.id)
		Core().create(manager2.id, client4.id)
		Core().create(manager2.id, client5.id)
		Core().create(manager2.id, client5.id)

		return "Initialized"

	def showAllInfo(self):
		print(Core().showAll(self.__ADMIN_PASSWORD))

	def demo(self):
		print("\nTask 2 DEMO")

		client1 = Authorizarion().clientAuhorization("c1", "c1")

		if (not client1):
			print("Error in Authorizarion to client1")
			return 

		print("Authorize like client 1: ", client1.id, client1.name)
		client1BankAccounts = client1.showMyBankAccounts()

		if (not client1BankAccounts):
			print("Error in Authorizarion to client1BankAccounts")
			return 
		
		client1BankAccountsString = "; ".join([str(bankAccount) for bankAccount in client1BankAccounts])

		print("Client 1 bank accounts:", client1BankAccountsString)
		
		client1FirstAccountId = client1BankAccounts[0].id

		print("Client 1 first account ballance: ", client1.showBankAccountBalace(client1FirstAccountId))

		manager1 = Authorizarion().managerAuthorization("m1", "m1")
		print("Authorize like manager 1")

		if (not manager1):
			print("Error in Authorizarion to manager1")
			return 

		manager1.replenishment(client1.id, client1FirstAccountId, 100)
		print("Manager 1 replenishment to client 1 bank account 1 +100$")
		
		print("Client 1 first account ballance: ", client1.showBankAccountBalace(client1FirstAccountId))
