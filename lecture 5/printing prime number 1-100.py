for j in range(1,101):
    n=j
    for i in range(2,n+1):   
        if(i<n and n%i==0):
            break 
        if(n==i):
            print(i)