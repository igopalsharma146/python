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
sumofdigit(eval(input("Enter any four digit number.")))