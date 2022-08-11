import json

class Category:
    
    __LEDGER_AMOUNT = 'amount'
    __LEDGER_DESCRIPTION = 'description'

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []
        self.balance = float(0.0)

    def get_category(self): return self.budget_category

    def deposit(self, amount, description = ''):
        self.ledger.append(self.__build_ledger_entry(amount, description))
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.balance >= amount:
            self.ledger.append(self.__build_ledger_entry(amount * float(-1), description))
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, category):
        if self.balance >= amount:
            local_ledger_entry_descr = 'Transfer to {}'.format(category.get_category())
            local_ledger_entry = self.__build_ledger_entry(float(-1) * amount, local_ledger_entry_descr)
            self.ledger.append(local_ledger_entry)
            self.balance -= amount
            other_ledger_entry_descr = 'Transfer from {}'.format(self.get_category())
            category.deposit(amount, other_ledger_entry_descr)
            return True
        else:
            return False

    def __build_ledger_entry(self, amount, description):
        return { \
            Category.__LEDGER_AMOUNT: amount, \
            Category.__LEDGER_DESCRIPTION: (description if description is not None else '')}



def create_spend_chart(categories):
    pass