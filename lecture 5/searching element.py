list=[1,2,3,54,6,7,8,9,9,"hello","mitrc",22.9]
list.append(78)
print(list)
n=eval(input("enter the value that you want to find."))
for i in range(0,len(list)):
    if(list[i]==n):
        print("value is found at index:",i)
        break #for stoping the loop
    else:
        print("value is not found.")