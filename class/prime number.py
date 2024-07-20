n=eval(input('Enter a numbar.'))
i=2
while(i<n):
    if(n%i==0):
        print("This number is not a prime.")
        exit(0)
    i=i+1
if(i==n):
    print("This number is prime number.")