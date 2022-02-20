class Category:
    def __init__(self,name):
        # Initialize the name of the budget
        self.name = name
        # Initialize an empty list to fill with transactions
        self.ledger = [ ]
        return
    
    def __str__(self):
        # Print the top bar of *** with the name centered
        printString = self.name.center(30,'*') + '\n'
        
        # for each transaction in the ledger
        for i in range(len(self.ledger)):
            # print the description
            printString += self.ledger[i]['description'][:23].ljust(23,' ')
            # and the amount of money for that item.
            printString += ('{:.2f}'.format(float(self.ledger[i]['amount']))).rjust(7,' ')
            # Dont forget the new line. 
            printString += '\n'

        # Print total amount of money for this category.
        printString += 'Total: ' + str('{:.2f}'.format(self.get_balance()))
        return printString

    def deposit(self, amount, description = ''):
        # Add an item to the ledger. This item gets added in as a Dictionary of 
        # amount and description. 
        self.ledger.append({'amount': amount, 'description': description})
        return

    def withdraw(self, amount, description = ''): 
        sufficientFunds = self.check_funds(amount)
        if sufficientFunds:
            self.ledger.append({"amount": -amount, "description": description}) 
        return sufficientFunds

    def get_balance(self):
        # Set an initial counting variable to zero. 
        balance = 0
        # For each transaction,
        for transaction in self.ledger:
            # Add up the money. Deposits are positive, and withdraws are negative.
            balance += transaction['amount']
        # Return the final amount for this category. 
        return balance

    def transfer(self,amount, account): 
        # First, check to see if there are sufficient funds in this account to
        # that could be transferred to another account. 
        sufficientFunds = self.check_funds(amount)

        # If there is enough money,
        if sufficientFunds: 
            # Withdraw the amount from here,
            self.withdraw(amount,'Transfer to ' + account.name)
            # and make a deposit to the destination account. 
            account.deposit(amount,'Transfer from ' + self.name)
        
        # Return whether this account had enough funds. If true, the transfer
        # took place. Otherwise, it did not. 
        return sufficientFunds

    def check_funds(self,amount): 
        # Get the balance for this account. 
        balance = self.get_balance()
        # Find the difference betweenthe desired withdraw, and the actual balance. 
        diff = balance - amount
        # If that difference is negative, there is not enough money. 
        if diff < 0:
            # Return false, as in there are not sufficient funds. 
            return False
        # If this point is reached, the diff was positive, and therefore, there
        # are sufficient funds. 
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
            if transaction['amount'] < 0: 
                # Subtract negative number to create positive spending amount. 
                catSpending -= transaction['amount']

            # Append total spent on current category to list created above.
        spendingList.append(catSpending)
    
    # Calculate the total spending to find percentage of each category.
    totalSpending = sum(spendingList)

    # Start creating the string to be printed. Saved as a list of lines. 
    printStringList = [ 'Percentage spent by category' ]

    # labels for Y-axis
    percentages = range(100, -1, -10)

    # Add label and axis to each line in graph.
    for percent in percentages:
        printStringList.append(str(percent).rjust(3,' ') + '| ')
    
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
                printStringList[i] += 'o  '

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

    # Logic of above loop includes a extra line of whitespace.
    # This whitespace causes tests to fail. 
    printStringList.pop()

    # Save the first string to the final string to be returned. 
    finalString = printStringList[0]
    
    # For every line in the list, starting with the second,
    for line in printStringList[1:]:
        # Add it as a new line to the string to be returned. 
        finalString += '\n' + line

    # Return the final string to be printed. 
    return finalString