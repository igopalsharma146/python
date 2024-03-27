m=eval(input("Enter first number:"))
n=eval(input("Enter second number:"))
a=m
b=n
(m,n)=(n,m)
s="Before swapping m={0} n={1} . And after swapping m={2} n={3}"
print(s.format(a,b,m,n))