def prime(n):
    i=2
    while(i<n):
        if(n%i==0):
            print("This number is note prime.")
            exit(0)
        i=i+1
    if(i==n):
        print("This number is prime number.")
n=eval(input('Enter a numbar.'))
prime(n)


def prime(n):
    i=2
    while(i<n):
        if(n%i==0):
            return False
            exit(0)
        i=i+1
    if(i==n):
        return True
n=eval(input('Enter a numbar.'))
print(prime(n))