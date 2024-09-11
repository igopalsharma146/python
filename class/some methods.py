# some methods in python

print("___________________ append ___________________")
l1=list([1,2,3,5])
l1.append('A')
print(l1)

print("___________________ clear ___________________")
l1=list([1,2,3,5])
l1.clear()
print(l1)


print("___________________ count ___________________")
l1=list([1,2,3,5,5,5,6])
x=l1.count(5)
print(l1)
print("count=",x)

print("___________________ copy ___________________")
l1=list([1,2,3,5,5,5,6])
x=l1.copy()
print(l1)
print("copied list=",x)

print("___________________ extend ___________________")
l1=list([1,2,3,5,5,5,6])
l2=list([88,99,77,66])
l2.extend(l1)
print(l2)

l1=list([1,2,3,5,5,5,6])
l2=list([88,99,77,66])
l1.extend(l2)
print(l1)

""" 
l1=list([1,2,3,5,5,5,6])
temp=l1
l2=list([88,99,77,66])
l1.extend(l2)
print(l1)
print(temp)
"""

print("___________________ index ___________________")
l1=list([1,2,3,5,5,5,6])
x=l1.index(5)
print(l1)
print("index=",x)

print("___________________ insert ___________________")
l1=list([1,2,3,5,5,5,6])
x=l1.insert(5,'A')
print(l1)


print("___________________ pop ___________________")
l1=list([1,2,3,5,5,5,6])
x=l1.pop(5)
l1.pop()
print(l1)