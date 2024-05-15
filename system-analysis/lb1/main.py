"""
1.3.2.29 Завдання:
а) У файлі містяться дані про товари на складах, що включають:
назва складу, адреса, відстань до складу, вартість постачання, назва
товару, вартість одиниці, кількість одиниць. Прочитати дані з файлу
та сформувати з них зв’язний список. Реалізувати пошук за списком
найдешевшого товару, заданого назвою.


б) Клієнт може мати декілька рахунків у банку.
Менеджер може
додавати,
переглядати,
редагувати (вносити кошти на рахунок)
та вилучати рахунки.

Клієнт може 
переглядати стан всіх своїх банківських рахунків (після авторизації),
сплачувати за послуги,
переглядати перелік операцій,
що вже відбулись.


Client
id
login
password
showBankAccountInfo(bankAccountId)
widhdrawMoneyFromBankAccount(bankAccountId)
showBankAccountHistoty(bankAccountId)

Manager
id
login
password

createNewBankAccount(clientId)
showBankAccountInfo(clientId, bankAccountId)
// поповнення
deleteBankAccount(clientId, bankAccountId)

Bank
clients
managers
bankAccounts

authorization(
login
password
accountType
): Client | Manager




BankAccountManager
accessLevel
clientId?

create(clientId)
showInfo(clientId, bankAccountId)
replenishment(clientId, bankAccountId, money)
delete(clientId, bankAccountId)
showHistoty(clientId, bankAccountId)
withdraw(clientId, bankAccountId, money)

BankAccount
id
clientId
balance
history

showInfo()
showHistory()


"""

from consolemenu import *
from consolemenu.items import *

from task1.task1Menu import task1ConsoleMenu 
from task2.task2Menu import task2ConsoleMenu
# from task2.task2 import Task2

# task2 = Task2()
# task2.initializeBaseStructureAsAdmin()
# task2.showAllInfo()
# task2.demo()

menu = ConsoleMenu("LB 1 System analysis")
menu.append_item(SubmenuItem("Task 1", task1ConsoleMenu))
menu.append_item(SubmenuItem("Task 2", task2ConsoleMenu))

# test()
menu.show()
