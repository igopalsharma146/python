n=eval(input("Enter the value that where want prime numbers."))
for i in range(2,n+1):   
        if(i<n and n%i==0):
            print("not prime")
            break 
        if(n==i):
            print("is a prime number.")
