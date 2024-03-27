n=eval(input("Enter a number."))
sum=0 
res=0
temp=n
while(n>0):
    rem=n%10
    res=res+rem**3
    n=n//10
if(temp==res):
    print(temp,"is a armstrong number.")
else:
    print(temp,"is not a prime number.")