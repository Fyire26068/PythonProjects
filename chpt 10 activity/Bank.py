class ATM:
    balance = 20.00
    
    def deposit(amount):
        print(str.format("Depositing ${:.2f}", amount))
        balance = ATM.balance + amount
        return balance

    def withdraw(amount):
        if ATM.balance > amount:
            print(str.format("Withdrawing ${:.2f}", amount))
            balance = ATM.balance - amount
        else:
            print("Insufficent funds")
        return balance

    def getBalance():
        return balance
