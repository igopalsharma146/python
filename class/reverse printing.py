n=eval(input("Enter a number."))
res=0
temp=n
while(n>0):
    rem=n%10
    res=res*10+rem
    n=n//10
s="reverse of {0} is {1}"
print(s.format(temp,res))