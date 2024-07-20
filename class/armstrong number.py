def length(n):
    res=0
    while(n>0):
        n=n//10
        res=res+1
    return res

n=eval(input("Enter a number."))
res=0
temp=n
length=length(n)
while(n>0):
    rem=n%10
    res=res+rem**length
    n=n//10
if(temp==res):
    print(temp,"is a armstrong number.")
else:
    print(temp,"is not a armstrong number.")