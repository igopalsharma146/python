n=int(input("enter the value of N :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i+j==n-1 and i<=n/2+1) or i+j==n+n//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")