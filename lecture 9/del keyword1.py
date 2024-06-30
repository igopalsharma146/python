class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        
acc1=Account('123456','ABCD')
print(acc1.acc_no)
print(acc1.acc_pass)