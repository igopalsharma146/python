def binary(array,target):
    left,right= 0,len(array)-1
    while left<=right:
        mid=(left+right)//2
        if (array[mid]==target):
            return mid
        elif(array[mid]<target):
            left=mid+1
        else:
            right=mid-1
    return -1
array=[45,7,8,3,56]
array.sort()
print(array)
target=eval(input("enter the number:"))
l1=binary(array,target)
if l1!=-1:
    print("The item is at:",l1+1)
else:
    print("Item does not exist.")