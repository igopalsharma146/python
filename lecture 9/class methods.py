'''
Class method:
            A class method is bound to the class and receives the class as an implicit first argument.
            Note:-static method can't access or modify the class state & generate for utility.
            
            
class student:
    @classmethod   #decoder
    def college(cls):
        pass
'''
class Person:
    name="gopi"
    
    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("GOPAL SHARMA")
print(p1.name)
print(Person.name)
print("------------------------------------------------------------------------------------------------")

class Person:
    name="gopi"
    
    def changeName(self,name):
        Person.name=name

p1=Person()
p1.changeName("GOPAL SHARMA")
print(p1.name)
print(Person.name)
print("------------------------------------------------------------------------------------------------")

class Person:
    name="gopi"
    
    def changeName(self,name):
        self.__class__.name="GOPAL"

p1=Person()
p1.changeName("GOPAL SHARMA")
print(p1.name)
print(Person.name)
print("------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------")
class Person:
    name="gopi"
    
    #def changeName(self,name):
        #self.__class__.name="GOPAL"
    
    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("GOPAL SHARMA")
print(p1.name)
print(Person.name)
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")