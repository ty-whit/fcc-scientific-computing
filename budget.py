class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = [ ]
        return

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})
        return

    def withdraw(self,amount, description): 
        if self.check_funds(amount):
            self.ledger.append({"amount": -1 * amount, "description": description})
        return 

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self): 
        pass

    def check_funds(self,amount): 
        pass


def create_spend_chart(categories):
    pass
