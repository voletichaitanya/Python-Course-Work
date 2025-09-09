from abc import ABC, abstractmethod

class Bankaccount(ABC):
    def deposit(self):
        print('you can deposit the amount')
    def checkbalance(self):
        print('ypu can check your balance')

    @abstractmethod
    def withdraw(self):
        pass
    def viewhistory(self):
        print('you can check the history')

class CurrentAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw Extra amount')

class SavingAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw the amount')

mani=CurrentAccount()
shanmukh=SavingAccount()
mani.checkbalance()
mani.deposit()
mani.viewhistory()
mani.withdraw()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.viewhistory()
shanmukh.withdraw()


from abc import ABC, abstractmethod
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: check chef availability, estimate time ")
class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order : check inventory per item, bag & space")
class MedicineOrder(Order):
    def process_order(seelf):
        print("Processing Medicine Order : Validate Prescription , assign secure")

rasool = FoodOrder()
chaitu = GroceryOrder()
swathi = MedicineOrder()

rasool.process_order()
chaitu.process_order()
swathi.process_order()



