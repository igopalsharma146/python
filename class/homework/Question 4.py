"""
    4).A four digit number is enter thorogh the keyword . write a program to calculate the sum of four digit number from both recursion or without recursion.
    """
def sumofdigit(n):
    sum=0
    temp=n
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    s="sum of digits is {0} if given number {1}"
    print(s.format(sum,temp))
sumofdigit(eval(input("Enter any four digit number:")))


# By recursion
def sumofdigit(n):
    rem=0
    if n==1:
        return 1
    elif n==0:
        return 0
    while(n>0):
        rem=n%10
        n=n//10
        return rem+sumofdigit(n)
temp=sumofdigit(eval(input("Enter any four digit number:")))
s="sum of digits is {0}."
print(s.format(temp))
