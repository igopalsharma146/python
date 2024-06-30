#printing sum of n natural numbers.
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
sum1=sum(eval(input("enter a number: ")))
print(sum1)