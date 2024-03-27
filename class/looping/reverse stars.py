n=eval(input("Enter a number:"))
for i in range (0,n//2+1):
    for j in range (0,i):
        print(" ",end=" ")
    for k in range (0,n-2*i):
        print("*",end=" ")
    print("\n")