from .libs.LinkedList import LinkedList
import csv
from .entities.Warehouse import Warehouse

class Task1:
	linkedList = LinkedList()	

	def readFromFileAndCreateLinkedList(self):
		with open("./task1/data/first-task-data.csv", newline="") as csvfile:
			reader = csv.reader(csvfile, delimiter=",", quotechar="|")

			next(reader)

			for row in reader:
				self.linkedList.inserAtEnd(Warehouse(*row))
			
			return "ok"

	def showLinkedList(self):
		return self.linkedList.getStringForDisplay()

	def findByName(self, name):
		return self.linkedList.find(name)
	
	def findByNameWithNameInput(self):
		name = input("Input name:")
		return self.linkedList.find(name)