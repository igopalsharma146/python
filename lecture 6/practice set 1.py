#write a function to print the length of list.(list is the parameter)
list=["alwar","mumbai","channai","goa","canada"]
list1=[2,3,4,6,7,5,4,8]
def print_len(n):
    print(len(n))
print_len(list)
print_len(list1)


#write a function to print the elements of a list in a single line.(list is the parameter)
def print_list(n):
    for item in n:
        print(item,end=" ")
print_list(list)
print("\n")
print_list(list1)
print("\n")
print("\n")

#write a function to find factorial of n.
def fact(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
        s="factorial of {0} is {1}."
    print(s.format(n,fact))
fact(eval(input("Enter the value that you want to find the factorial:")))
fact(eval(input("Enter the value that you want to find the factorial:")))
fact(eval(input("Enter the value that you want to find the factorial:")))
print("\n")


#write a function to convert USD to INR.
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")
converter(73)