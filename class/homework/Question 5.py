"""
    5) write a program to calculate the gcd.the function should take positive integer and return.
    """
def gcd(a,b):
    temp1=a
    temp2=b
    i=2
    gcd=1
    while((a and b)>=i):
        if(a%i==0 and b%i==0):
            gcd=gcd*i
            a=a//i
            b=b//i
            i=2
        elif((a and b)<i):
            gcd=1
        i=i+1
    s="gcd of {0},{1} is {2}"
    print(s.format(temp1,temp2,gcd))
gcd(eval(input("enter first value:")),eval(input("enter second value:")))

def gcd(a,b):
    temp1=a
    temp2=b
    i=2
    gcd=1
    while((a and b)>=i):
        if(a%i==0 and b%i==0):
            gcd=i
        elif((a and b)<i):
            gcd=1
        i=i+1
    s="gcd of {0},{1} is {2}"
    print(s.format(temp1,temp2,gcd))
gcd(eval(input("enter first value:")),eval(input("enter second value:")))