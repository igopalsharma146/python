'''
i). Define a circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
define a perimeter() method of the class which allows you to calculate the perimeter of the circle.
'''
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1=Circle(21)
print(c1.Area())
print(c1.perimeter())
print("----------------------------------------------------------------------------------------------")





'''
ii).Define a Employee class with attributes role,department and salary. This class also
showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional
attributes : name & age.
'''
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
        
class Engineer(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")
        
# e1=Employee("Accountant","Finance","60,000")
# e1.showDetails()

engg1=Engineer("GOPAL SHARMA",22)
engg1.showDetails()

print("----------------------------------------------------------------------------------------")

'''
iii).Create a class order which stores item & its Price.
    Use Dunder function __gt__() to convey that:
        order1>order2 if price of order1>order2
'''
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,ord2):
        return self.price>ord2.price
    
        
ord1=Order("chips",20)
ord2=Order("tea",15)

print(ord1>ord2)