# create a program to print and store sqare of numbers into dictionary.
def square(num):
    dict={}
    i=1
    while(i<=num):
        dict.update({i:i**2})
        i+=1
    print(dict)
n=eval(input("Enter a Number : "))
square(n)