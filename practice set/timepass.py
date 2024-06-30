n = int(input("Enter the value of n: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end ="")
    for k in range(0,i*2+1):
        print("*",end="")
    print("\n",end="")
for i in range(0,3):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range(0,n-i*2+1):
        print("*",end="")
    print("\n",end="")