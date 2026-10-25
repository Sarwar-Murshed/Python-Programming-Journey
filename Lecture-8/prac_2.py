"""
Create Account class with 2 attributes balance and account no. Create methods for debit,
credit and printing the balance """

class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

# debit method

    def debit(self,amount):
        self.bal -= amount
        print("USD",amount,"was debited")
        print("Total Balance :",self.getBalance())

# credit method

    def credit(self,amount):
        self.bal += amount
        print("USD",amount,"was credited")
        print("Total Balance :",self.getBalance())
        print()

    def getBalance(self):
        return self.bal

acc1 = Account(20000,18975)
print("Balance : ",acc1.bal)
print("Account NO. : ",acc1.acc)
print()

acc1.debit(5000)
acc1.credit(8000)

acc1.debit(1000)
acc1.credit(1500)
