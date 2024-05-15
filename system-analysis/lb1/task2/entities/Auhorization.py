from typing import Union
from task2.entities.Client import Client
from task2.entities.Manager import Manager
from .Core import Core

class Authorizarion():
	__core = Core()

	def clientAuhorization(self, login, password) -> Union[Client, None]:
		return self.__core.authorizarion("client", login, password)
	
	def managerAuthorization(self, login, password) -> Union[Manager, None]:
		return self.__core.authorizarion("manager", login, password)