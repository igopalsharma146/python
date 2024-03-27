def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
s="fact of {0} is {1}."
n=eval(input("enter the number where that you want to find fact:"))
print(s.format(n,fact(n)))
n=eval(input("enter the number where that you want to find fact:"))
print(s.format(n,fact(n)))
n=eval(input("enter the number where that you want to find fact:"))
print(s.format(n,fact(n)))