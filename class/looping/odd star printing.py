n=eval(input("enter the number:"))
for i in range (1,n//2+2):
    for j in range (0,n//2-i+1):
        print(" ",end=" ")
    for k in range (0,2*i-1):
        print("*",end=" ")
    print("\n")