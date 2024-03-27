n=eval(input("Enter a number:"))
for i in range (1,n):
    for j in range (1,n+1-i):
        print("*",end=" ")
    print("\n")
for i in range (1,n-1):
    for j in range (1,i+2):
        print("*",end=" ")
    print("\n")