import Bank
import Input

balance = ATM.getBalance()

amount = Input.get_integer("Please enter deposit amount ($0.00 - $1000.00): ", 0.00, 1000.00)
balance = ATM.deposit(amount)
print(str.format("New Balance: ${:.2f}", balance))

amount = Input.get_integer("Please enter withdrawal amount ($0.00 - $1000.00): ", 0.00, 1000.00)
balance = ATM.withdraw(amount)
print(str.format("New Balance: ${:.2f}", balance))
