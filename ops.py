import os

class BankAccount:
    def __init__(self, balance):
        self.balance = balance  

    def widthdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance!')
            return -1
        self.balance -= amount 
        print('Withdrawal of {0} successful! New balance is {1}.'.format(amount, self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print('Deposit of {0} successful! New balance is {1}'.format(amount, self.balance))
        return self.balance

    def balance_check(self):
        print('You have a balance of {0}'.format(self.balance))
        return self.balance
    

if __name__ == '__main__':
    pass