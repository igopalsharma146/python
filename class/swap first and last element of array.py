# Swapping first and last element of 1D Array

#Without third variable
print("Without third variable")
def swap(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    print("After Swap :",arr)
    
import numpy as np
arr=np.array([2,3,5,73,6,4])
print("Before Swap :",arr)
swap(arr)

print("\n-----------------------------------------------------------------------------------------------\n")

#By using third variable
print("By using third variable")
def swap(arr):
    temp=arr[0]
    arr[0]=arr[-1]
    arr[-1]=temp
    print("After Swap :",arr)
    
import numpy as np
arr=np.array([2,3,5,73,6,4])
print("Before Swap :",arr)
swap(arr)
