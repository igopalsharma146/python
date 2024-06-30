'''
CLASS & INSTANCE ATTRIBUTE:Class.attr
obj.attr
'''
class Student :
    college_name="MITRC COLLEGE ALWAR"
    name ="gopi"        #class atributes
    
    def __init__(self,name ,age):
        self.name =name #object attribute
        self.age=age
        print("adding new student in the database")
s1=Student("rohan",40)
print(s1.name)
s2=Student("gopal sharma",20)
print(s2.name)
print(s2.college_name)