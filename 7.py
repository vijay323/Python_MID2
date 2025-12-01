"""Q7. Define a class Bank Account with attributes like account number, name, and balance. 
Implement methods for deposit, withdrawal, and displaying account information."""
class BankAccount: 
    def __init__(self, acc_no, name, balance=0): 
        self.acc_no = acc_no 
        self.name = name 
        self.balance = balance 
 
    def deposit(self, amt): 
        self.balance += amt 
        print("Deposited:", amt) 
 
    def withdraw(self, amt): 
        if amt <= self.balance: 
            self.balance -= amt 
            print("Withdrawn:", amt) 
        else: 
            print("Insufficient balance") 
 
    def display(self): 
        print(f"Account No: {self.acc_no}, Name: {self.name}, Balance: {self.balance}") 
 
acc = BankAccount(101, "Vijay", 5000) 
acc.deposit(2000) 
acc.withdraw(1500) 
acc.display() 
