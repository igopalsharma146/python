'''
STATIC METHODS:Methods that don't use the self parameter (work at last level)

class student:
    @staticmethod #decorator
    def college():
        print("MITRC COLLEGE.")
        
"Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
without parmanently modifying it.
"
'''
class student:
    @staticmethod #decorator
    def college():
        print("MITRC COLLEGE.")
s1=student()
print(s1.college())