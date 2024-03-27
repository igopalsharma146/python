"""
Q:1->Write a program using while loop which prints the sum of every fifth number from 0 to 500.
(including both 0 and 500)
    """
i=0
sum=0
while (i<=500):
    temp=i
    print(temp,end=" ")
    sum=sum+i
    if (i%5==0):
        print("\nsum of next five number is : ",sum)
        sum=0
    i=i+1
