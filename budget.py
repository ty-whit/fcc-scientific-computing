class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = [ ]
        return

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        return

    def withdraw(self, amount, description = ""): 
        sufficientFunds = self.check_funds(amount)
        if sufficientFunds:
            self.ledger.append({"amount": -amount, "description": description}) 
        return sufficientFunds

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self,amount, account): 
        sufficientFunds = self.check_funds(amount)
        if sufficientFunds: 
            self.withdraw(amount,"Transfer to " + account.name)
            account.deposit(amount,"Transfer from " + self.name)
        return sufficientFunds

    def check_funds(self,amount): 
        balance = self.get_balance()
        diff = balance - amount
        if diff < 0:
            return False
        return True

def create_spend_chart(categories):
    # amount spent by each category 
    spendingList = []

    # Loop through each of the categories given to display
    for cat in categories: 
        # Amount spent by current category  in loop
        catSpending = 0

        # Loop through each category
        for transaction in cat.ledger:
            # If transaction was positive, it was a deposit. 
            # If negative, it was money spent. 
            if transaction["amount"] > 0: 
                # Subtract negative number to create positive spending amount. 
                catSpending -= transaction["amount"]

            # Append total spent on current category to list created above.
        spendingList.append(catSpending)
    
    # Calculate the total spending to find percentage of each category.
    totalSpending = sum(spendingList)

    # Start creating the string to be printed. Saved as a list of lines. 
    printStringList = [ "Percentage spent by category" ]

    # labels for Y-axis
    percentages = range(100, -1, -10)

    # Add label and axis to each line in graph.
    for percent in percentages:
        printStringList.append(str(percent).rjust(3," ") + "| ")
    
    # Draw bar for each category  
    for cat in range(len(categories)):
        # Loop through each percent amount to see if the bar reaches this high. 
        for i in range(1,len(printStringList)):
            # if spending amount is greater than current percent
            if spendingList[cat] / totalSpending * 100 < percentages[i-1]: 
                # else, draw empty space
                printStringList[i] += '   ' 
            else: 
                # then draw a dot 
                printStringList[i] += "o  "

    # Draw the bottom line that forms the x-axis
    printStringList.append('    '.ljust(len(printStringList[-1]),'-'))

    # Counting variable used to write names under bars
    count = 0
    # flags to determine if we are still writing the names. 
    addingCharacters = [True, True, True]

    # While we are still adding characters
    while addingCharacters[0] or addingCharacters[1] or addingCharacters[2]:
        # Indentation required for graph
        newLine = '     '
        # Loop over each category
        for j in range(len(categories)):
            # Are we adding characters on this category?
            if addingCharacters[j]: 
                # Try to add the next character
                try: 
                    newLine += categories[j].name[count] + '  '
                # if we have reached the end of the string
                except IndexError:
                    # Add white space under the word
                    newLine += '   '
                    # Change this flag to false.
                    addingCharacters[j] = False
            # if we have reached the end of this word
            else:  
                # Add white space under category word
                newLine += '   '
        # move to next character in word
        count += 1

        printStringList.append(newLine)

    finalString = ''

    for line in printStringList:
        finalString += line + "\n"

    return finalString