n=eval(input("Enter a number."))
fact=1
for i in range (1,n+1):
    fact=fact*i
s="factorial of {0} is {1}."
print(s.format(n,fact))