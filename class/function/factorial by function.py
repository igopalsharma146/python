def fact(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
        s="factorial of {0} is {1}."
    print(s.format(n,fact))
fact(eval(input("Enter the value that you want to find the factorial:")))
fact(eval(input("Enter the value that you want to find the factorial:")))
fact(eval(input("Enter the value that you want to find the factorial:")))