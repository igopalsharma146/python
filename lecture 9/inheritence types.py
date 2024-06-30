'''
i) Single inheritence (base class --> derived class)
ii) multi-level inheritence (base class --> derived class --> derived class)
iii)multiple inheritence ((base class 1 , base class 2) --> derived class)
'''

# Single inheritence (base class --> derived class)
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
print("-----------------------------------------------------------------------------------------------")

#multi-level inheritence
class Car:
    
    @staticmethod
    def start():
        print("car is started....")
        
    @staticmethod
    def stop():
        print("car is stopped....")

class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand
        
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
    
car1=Fortuner("diesel")

print(car1.start())
print(car1.type)
print("-----------------------------------------------------------------------------------------------")


#multiple inheritence ((base class 1 , base class 2) --> derived class)

class A:
    varA="Welcome to class A"
    
class B:
    varB="Welcome to class B"
    
class C(A,B):
    varC="Welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)