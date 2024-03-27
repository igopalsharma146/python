""" 
Recursion:-when a function calls itself repeatedly.

#print n to 1 backwards

"""
#example
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(eval(input("enter a number.")))