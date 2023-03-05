"""Create a python class called BankAccount with attributes like account_number, balance,
date_of_opening and customer_name and methods like deposit, withdraw, check_balance and customer_details

i. The deposit method should return the amount deposited
ii. The withdraw method should return insufficient balance if account is less than amount to be
withdrawn else it should return the amount that has been withdrawn
iii. The check_balance method should print the current balance
iv. The customer_details method should print customer name, account number, date of account opening 
and balance"""

#A Program to help in the customer care desk

account_number = int(input("Enter your account number : "))
date_of_opening = input("Enter the date of opening the account : ")
customer_name = input("Enter the customer name here : ")
amount_deposited = float(input("Enter the amount deposited Kshs : "))
amount_to_withdraw = float(input("Enter the amount you want to withdraw Kshs : "))
initial_balance = float(input("Enter the inital amount in the account/opening amount Kshs : "))
account = initial_balance + amount_deposited
balance  = account - amount_to_withdraw

if account < amount_to_withdraw:
    print("Insufficient Balance...Please Top up you account!!!")
else:
    print("You are allowed to Proceed")

class BankAccount:
    def __init__(self,initial_balance,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        self.initial_balance  = initial_balance

    def deposit(self):
        return amount_deposited

    def withdrawal(self):
        return amount_to_withdraw

    def check_balance(self):
        return balance
        
    def customer_details(self):
        return (customer_name,account_number,date_of_opening)


bank = BankAccount(initial_balance,account_number,balance,date_of_opening,customer_name)

print("You deposited Kshs : ", bank.deposit())
print("This is the amount you have requested to withdraw Kshs : ", bank.withdrawal())
print("Your current balance is Kshs : ", bank.check_balance())
print("Here are the customer details (name,account_no,opening_date) : ", bank.customer_details())


