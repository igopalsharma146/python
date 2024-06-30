'''
we use @property decorator on any method in the class to use the method as a property.

'''

class Student:
    def __init__(self,phy ,chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
print(stu1.percentage) 
#here percentage is not change but we are want to change the percentage then we are use here methods.


print("-----------------------------------------------------------------------------------------------")
class Student:
    def __init__(self,phy ,chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
    def calculatepercentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
stu1.calculatepercentage()
print(stu1.percentage) 
print("-----------------------------------------------------------------------------------------------")

#but isse better tarika property decoretor hai.
class Student:
    def __init__(self,phy ,chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math        
    # def calculatepercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    
    @property
    def calculatepercentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,99)
print(stu1.calculatepercentage) 

stu1.phy=86
print(stu1.phy)
print(stu1.calculatepercentage) 

#two more decoretors here getter and setter. we can do read these 