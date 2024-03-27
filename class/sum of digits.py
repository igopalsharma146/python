n=eval(input("Enter a number."))
res=0
temp=n
while(n>0):
    rem=n%10
    res=res+rem
    n=n//10
s="Sum of digits is {1} of given number {0}"
print(s.format(temp,res))