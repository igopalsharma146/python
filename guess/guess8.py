print("\n-------------------average finding------------------------\n")
def avg(a=1, b=5):
    print(a)
    print(b)
    print("average=",(a+b)/2)
avg()
avg(5)
avg(5,6)
avg(a=17)
avg(b=17)
avg(b=17,a=6)


'''print("\n-------------------average finding------------------------\n")
def avg(x=1, y=5):
    print(x)
    print(y)
    print("average=",(x+y)/2)
avg()
avg(5)
avg(5,6)
avg(a=17) #these are showing the error
avg(b=17)
avg(b=17,a=6)'''


print("\n-------------------tupples------------------------\n")
def avg(*numbers):
    print(numbers)
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("average=",sum/len(numbers))
avg(2,3,4,5,6)



print("\n-------------------dictionary------------------------\n")
def avg(**name):
    print(name)
    print(type(name))
avg(fname="gopal",lname="sharma",branch="AI & ML")



print("\n-------------------dictionary------------------------\n")
def avg(**name):
    print(name)
    print(type(name))
    print("hello! Mr.",name["fname"],name["mname"],name["lname"])
avg(fname="Krishan",lname="sharma",mname="kumar")