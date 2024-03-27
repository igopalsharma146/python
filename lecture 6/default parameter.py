""" 
default parameter:-Assigning a default value to parameter,which is used when no argument is passed.
"""



"""
def mul(a,b):
    print(a*b)
    return a*b
mul()

"""
#default parameter
def mul(a=1,b=1):
    print(a*b)
    return a*b
mul()

#default parameter
def mul(a=1,b=1):
    print(a*b)
    return a*b
mul(3,4)

#default parameter
def mul(a,b=1):
    print(a*b)
    return a*b
mul(5)

