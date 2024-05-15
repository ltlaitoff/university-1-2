from consolemenu import *
from consolemenu.items import *
from task2.task2 import Task2

task2 = Task2()


task2ConsoleMenu = ConsoleMenu("LB 2 System analysis", "Task 1")

promptUtils = PromptUtils(Screen())

def intializeWrapper():
	result = task2.initializeBaseStructureAsAdmin()
	promptUtils.println(result)
	promptUtils.enter_to_continue()


def demoWrapper():
	result = task2.demo()
	promptUtils.println(result)
	promptUtils.enter_to_continue()


def showAllInfoWrapper():
	result = task2.showAllInfo()
	promptUtils.println(result)
	promptUtils.enter_to_continue()

task2ConsoleMenu.append_item(FunctionItem("Initialize", intializeWrapper ))
task2ConsoleMenu.append_item(FunctionItem("Show all elements", showAllInfoWrapper))
task2ConsoleMenu.append_item(FunctionItem("Demo", demoWrapper))

