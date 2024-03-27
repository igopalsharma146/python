#printing sum of n natural numbers.
def show(n):
    if(n==0):
        return 0
    else:
        return n+show(n-1)
sum1=show(eval(input("enter a number.")))
print(sum1)