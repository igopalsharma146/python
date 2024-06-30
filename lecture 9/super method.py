'''
super() method is used to access methods of the parent class.
'''
class Car:
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("car is started....")
        
    @staticmethod
    def stop():
        print("car is stopped....")

class Toyotacar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
        
car1=Toyotacar("prius","electric")
print(car1.name)
print(car1.type)