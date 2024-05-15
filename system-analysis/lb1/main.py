"""
1.3.2.29 Завдання:
а) У файлі містяться дані про товари на складах, що включають:
назва складу, адреса, відстань до складу, вартість постачання, назва
товару, вартість одиниці, кількість одиниць. Прочитати дані з файлу
та сформувати з них зв’язний список. Реалізувати пошук за списком
найдешевшого товару, заданого назвою.


б) Клієнт може мати декілька рахунків у банку. Менеджер може
додавати, переглядати, редагувати (вносити кошти на рахунок) та
вилучати рахунки. Клієнт може переглядати стан всіх своїх
банківських рахунків (після авторизації), сплачувати за послуги,
переглядати перелік операцій, що вже відбулись.
"""

import csv
from entities.Warehouse import Warehouse
from libs.LinkedList import LinkedList

linkedList = LinkedList()	

with open("./data/first-task-data.csv", newline="") as csvfile:
	reader = csv.reader(csvfile, delimiter=",", quotechar="|")

	next(reader)

	for row in reader:
		linkedList.inserAtEnd(Warehouse(*row))
		
	linkedList.print()

print(linkedList.find("Sauer").name)
