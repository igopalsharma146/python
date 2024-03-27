def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=eval(input("enter the number where that you want to do sum:"))
s="sum of {0} number from starting is {1}."
print(s.format(n,sum(n)))
n=eval(input("enter the number where that you want to do sum:"))
print(s.format(n,sum(n)))
n=eval(input("enter the number where that you want to do sum:"))
print(s.format(n,sum(n)))