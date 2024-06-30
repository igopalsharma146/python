def reverse(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("Reverse number is :",rev)
n=int(input("Enter the number that you want to reverse :"))
reverse(n)