'''
When one class(child/derived)derives the properties & methods of another class(parent/base).

class car:
        ........
        ........
        ........
        
class toyotoCar(car):
        ...........
        ...........
        ...........
'''
class Car:
    color="black"
    
    @staticmethod
    def start():
        print("car is started....")
        
    @staticmethod
    def stop():
        print("car is stopped....")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
    
car1=Toyotacar("Fortuner")
car2=Toyotacar("prius")

print(car1.start())
print(car1.stop())
print(car1.color)