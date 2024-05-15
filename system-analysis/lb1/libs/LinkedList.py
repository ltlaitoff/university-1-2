from typing import Self
from entities import Warehouse

class LinkedListNode:
	def __init__(self, value: Warehouse):
		self.value = value
		self.next = None 


class LinkedList:
	def __init__(self):
		self.head = None

	def inserAtEnd(self, value: Warehouse):
		new_node = LinkedListNode(value)

		if self.head is None:
				self.head = new_node
				return
		
		current_node = self.head
		while(current_node.next):
				current_node = current_node.next

		current_node.next = new_node

	def print(self):
		arrayForPrint = []
	
		current_node = self.head
		while(current_node.next):
			arrayForPrint.append(current_node.value)
			current_node = current_node.next

		resultString = ""

		for element in arrayForPrint:
			resultString += element.name[:5] + " => "

		print("Linked list:", resultString)
	
	def find(self, name):
		current_node = self.head
		arrayOfElements = []
		
		while(current_node.next):
			if (current_node.value.name.startswith(name)):
				arrayOfElements.append(current_node.value)
			current_node = current_node.next

		arrayOfElements.sort(key=lambda x: x.unit_cost)

		# for element in arrayOfElements:
		# 	print(element.name, element.unit_cost)

		return arrayOfElements[0]

