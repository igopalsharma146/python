'''
METHODS:methods are function that belong to objects.

#creating class
class student:
    def __init__(self,fullname):
        self.name=fullname
        
def hello(self):
    print("hello",self.name)
    
#creating object
s1=student("GOPAL")
s1.hello()


'''
#creating class
class student:
    fullname="gopal sharma"
    
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        
    def hello(self):
        print("hello",self.name)
        print("hello",self.fullname)
        
    def get_marks(self):
        return self.marks
#creating object
s1=student("GOPAL",99)
s1.hello()
print("marks=",s1.get_marks())