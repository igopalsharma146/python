"""
    3). Write a program to create a function to return the reverse of the number ended.
    """
def num(n):
    rev=0
    temp=n
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
        s="reverse of {0} is {1}."
    print(s.format(temp,rev))
num(eval(input("Enter the number that you want to do reverse:")))