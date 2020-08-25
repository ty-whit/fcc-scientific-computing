class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = [ ]
        return

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})
        return

    def withdraw(self,amount, description): 
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -1 * amount, "description": description}) 
        return funds

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self): 
        pass

    def check_funds(self,amount): 
        balance = self.get_balance()
        diff = balance - amount
        if diff < 0:
            return False
        return True


def create_spend_chart(categories):
    pass
