def linear(array,target):
    for i in range (len(array)):
        if array[i]==target:
            return i
    else:
        return -1
array=[45,7,8,3,56]
array.sort()
print(array)
target=eval(input("enter the number:"))
l1=linear(array,target)
if l1!=-1:
    print("The item is at:",l1+1)
else:
    print("Item does not exist.")