'''
2). Create account class with 2 attributes- balence & account number.
    create numbers for debit , credit & printing the balence.
'''
class account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.account_no=acc
        
    def debit(self,amount):
        self.balance -= amount
        print("\nRs.",amount,"was debited.")
        print("Total balance = ",self.get_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("\nRs.",amount,"was credited.")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
        
acc1=account(10000,44420100023890)
print("Total balance before debit or credit =",acc1.balance)
print("Account number=",acc1.account_no)
acc1.debit(1000)
acc1.credit(2000)