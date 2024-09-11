l1=[]
sum1=0
for i in range (0,5):
    l1.append(eval(input("enter a number:")))
for i in range(0,5):
    sum1=sum1+l1[i]
avg=sum1/len(l1)
print("average=",avg)

#using sum function
l2=[]
sum2=0
for i in range (0,5):
    l2.append(eval(input("enter a number:")))
sum2=sum(l2)
avg=sum2/5
print("average=",avg)