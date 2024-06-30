'''
Conceptual Implementation in python:
                                    Private atributes and methods are meant to be used only with in the class and are not accessible from outside the class.
                                    
                                    
kisi bhi cheej ki private banane ke liye uske aage two under score laga dete hai.
'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        
acc1=Account('123456','ABCD')
print(acc1.acc_no)
print(acc1.acc_pass)
print("----------------------------------------------------------------------------------------------")

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        
    def reset_pass(self):
        print(self.acc_pass)
        
acc1=Account('123456','ABCD')
print(acc1.acc_no)
print(acc1.reset_pass())
print("----------------------------------------------------------------------------------------------")

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
        
acc1=Account('123456','ABCD')
print(acc1.acc_no)
print(acc1.acc_pass)
print("----------------------------------------------------------------------------------------------")
