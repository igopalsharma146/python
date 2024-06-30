'''
Polymorphism:(Oerator overloding)
            when the same operator is allowed to have different meaning according to the context.
            
operator and dunder function:
a+b         #addition                  a.__add__(b)
a-b         #subtraction               a.__sub__(b)
a*b         #multiplication            a.__mul____(b)
a/b         #division                  a.__truediv____(b)
a%b         #remender                  a.__mod____(b)
'''

#implicit overloading
print(1+2) #3
print("GOPAL"+"SHARMA") #concatenate
print([1,2,3]+[4,5,6]) #merge

print("--------------------------------------------------------------------------------------------")

'''
complex numbers:
                normal(real) number = (1,2,-4,5.34 etc.)
                imagenary part= (3i,5i,7i,3.14i etc.)
                
                ex:
                5i+10j
                2i+13j
            -------------
                7i+23j

uses:voice recognization,machine learning.
'''
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i + ",self.img,"j")
        
    def add(num1,num2):
        newReal=num1.real + num2.real
        newImg=num1.img + num2.img
        return complex(newReal,newImg)
        
num1=complex(2,4)
print(num1.showNumber())

num2=complex(3,6)
print(num2.showNumber())

num3=num1.add(num2)
num3.showNumber()

print("-----------------------------------------------------------------------------------------------")
#but we are want to direct print the complex number . we are not want to write the method.
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i + ",self.img,"j")
        
    def __add__(num1,num2):
        newReal=num1.real + num2.real
        newImg=num1.img + num2.img
        return complex(newReal,newImg)
    
    def __sub__(num1,num2):
        newReal=num1.real - num2.real
        newImg=num1.img - num2.img
        return complex(newReal,newImg)
        
num1=complex(2,4)
print(num1.showNumber())

num2=complex(3,6)
print(num2.showNumber())

# num3=num1.add(num2)
# num3.showNumber()
num3=num1+num2
num3.showNumber()

num3=num1-num2
num3.showNumber()