import json

class Category:
    
    def get_amount_key(): return 'amount'
    def get_description_key(): return 'description'

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []
        self.balance = float(0.0)

    def __str__(self):
        line_length = 30
        result = self.get_category().center(line_length, "*")
        result += "\n"
        # show ledger
        for entry in self.ledger:
            valStr = "{:.2f}".format(entry[Category.get_amount_key()])
            remaining = line_length - len(valStr)
            curr_descr = entry[Category.get_description_key()]
            max_descr_len = remaining - 1
            cut_descr = min(len(curr_descr), max_descr_len)
            curr_descr = curr_descr[0:cut_descr]
            line = curr_descr.ljust(remaining, " ")
            line += valStr
            line += "\n"
            result += line
        total_line = "Total: {:.2f}".format(self.get_balance())
        result += total_line
        return result

    def get_category(self): return self.budget_category

    def get_ledger(self): return self.ledger

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
            Category.get_amount_key(): amount, \
            Category.get_description_key(): (description if description is not None else '')}



def create_spend_chart(categories):
    result = "Percentage spent by category\n"
    total_withdrawal = 0
    withdrawal_dict = {}
    withdrawal_perc_dict = {}
    max_category_len = 0
    for category in categories:
        max_category_len = max(max_category_len, len(category.get_category()))
        withdrawal = float(0)
        for entry in category.get_ledger():
            amount = entry[Category.get_amount_key()]
            if amount < 0:
                withdrawal -= amount
        withdrawal_dict[category.get_category()] = withdrawal
        total_withdrawal += withdrawal
    for category in categories:
        percentage = float(100) * (withdrawal_dict[category.get_category()] / total_withdrawal)
        withdrawal_perc_dict[category.get_category()] = percentage

    for i in range(100, -1, -10):
        line = "{:>3}|".format(i)
        for category in categories:
            if (withdrawal_perc_dict[category.get_category()] > i):
                line += " o "
            else:
                line += "   "
        line += " \n"
        result += line

    # separator line
    separation_line = "    "
    for x in range(len(categories)):
        separation_line += "---" 
    result += separation_line + "-\n" 
    for x in range(max_category_len):
        line = "    "
        for category in categories:
            if len(category.get_category()) >= (x + 1):
                line += " " + category.get_category()[x:x + 1] + " "
            else:
                line += "   "
        result += line + " "
        if x < (max_category_len - 1): result += "\n"
    return result