from consolemenu import *
from consolemenu.items import *
from task1.task1 import Task1

task1 = Task1()

def test():
	print(task1.readFromFileAndCreateLinkedList())
	print(task1.showLinkedList())
	print(task1.findByName("Conne"))

task1ConsoleMenu = ConsoleMenu("LB 2 System analysis", "Task 1")

promptUtils = PromptUtils(Screen())

def showLinkedListWrapper():
	result = task1.showLinkedList()
	promptUtils.println(result)
	promptUtils.enter_to_continue()


def findByNameWithNameInputWrapper():
	result = task1.findByNameWithNameInput()
	promptUtils.println(result)
	promptUtils.enter_to_continue()


def findByNameWithNameStatic(*params):
	result = task1.findByName("Sauer")
	promptUtils.println(result)
	promptUtils.enter_to_continue()

task1ConsoleMenu.append_item(FunctionItem("Read data from file", task1.readFromFileAndCreateLinkedList ))
task1ConsoleMenu.append_item(FunctionItem("Show linked list", showLinkedListWrapper))
task1ConsoleMenu.append_item(FunctionItem("Find by name", findByNameWithNameInputWrapper))
task1ConsoleMenu.append_item(FunctionItem("Find by static name 'Sauer'", findByNameWithNameStatic ))
