def even(x,y):
    l1=[]
    temp=x
    temp1=y
    if(temp%2==0):
        a=temp
        while (temp1>=a):
            l1.append(a)
            a+=2
        print(l1)
    elif(temp%2!=0):
        a=temp+1
        while (temp1>=a):
            l1.append(a)
            a+=2
        print(l1)
a=eval(input('enter first number:'))
b=eval(input('enter second number:'))
even(a,b)