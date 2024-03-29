#list operator

#plus operator
print("__________ plus operator ___________")
a=[1,2,3]
b=[4,5,6,8]
print(a+b)

# multiply operator
print("__________ multiply operator ___________")
l1=[1,2,3,4]
l2=2*l1
print(l2)

l1=[1,2,3,4]
l2=2*l1[3]
print(l2)

# in operator
print("__________ in operator ___________")
l1=[10,20,30,40]
print(l1)
print(40 in l1)

x= 3 in l1
print(x)

a="hello"
b="ll"
print(b in a)


# is operator
print("__________ is operator ___________")
a="hello"
b="hello"
x=b is a
print(x)

a=[10,20,10]
b=[10,20,10]
x=a==b
print(x)

a=[10,20,10]
b=[10,20,10]
x=b is a
print(x)


# del
print("__________ del operator ___________")
l1=[10,20,30]
del l1[2]
print(l1)