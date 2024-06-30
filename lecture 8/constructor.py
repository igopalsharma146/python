'''
CONSTRUCTOR:All classes have a function called _init_(), which is always executed when the object is being initiated.

#creating class
class student:
    def __init__(self,fullname):
        self.name=fullname
        
#creating object
s1=student("GOPAL")
print(s1.name)

'''

#the self parameter is a reference to the current instance of the class, and it used to access variables that belongs to the class.

class student:
    name="GOPAL SHARMA"
    def __init__(self):
        print("Adding new student in database...")
s1=student()

#here self mean hum s1 name ke object ki baat kar rahe hai.
class student:
    name="GOPAL SHARMA"
    def __init__(self):
        print(self)
        print("Adding new student in database...")
s1=student()
print(s1)


class student:
    name="GOPAL SHARMA"
    #it is a constructor, if we are not create any constructor then python will be automatically create a constructor for ours.
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new student in database...")
s1=student("GOPAL SHARMA")
print(s1.name)
s2=student("ARMAN KHAN")
print(s2.name)

#parameterized constructor
class student:
    name="GOPAL SHARMA"
    def __init__(self,fullname,marks,age):
        self.name=fullname
        self.marks=marks
        self.age=age
        print("Adding new student in database...")
s1=student("GOPAL SHARMA",99,20)
print("Name=",s1.name)
print("Marks=",s1.marks)
print("Age=",s1.age)
s2=student("ARMAN KHAN",100,20)
print("Name=",s2.name)
print("Marks=",s2.marks)
print("Age=",s2.age)