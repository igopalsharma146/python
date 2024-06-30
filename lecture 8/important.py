'''
ABSTRACTION:Hiding the implementation details of a class & only showing the essential features to the user.

ENCAPSULATION: Wrapping data and functions into a single unit(object). 
'''

# Example of Abstraction
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")
        
car1=car()
car1.start()
    
    
    
# Example of Encapsulation
