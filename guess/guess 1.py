def f(x ,y=[]):
    y.append(x)
    return y
y=[]
print(f(1))
print(f(2))

def fun(x,y,z=0):
    return x*y+z
print(fun(1,2,3))
print(fun(1,2))