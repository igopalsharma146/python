def bubble_short(array):
    n=len(array)
    for i in range (0,n-1):
        for j in range (0,n-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
            #print("pass:",i,array)
        print("pass:",i,array)
a1=[66,7,3,45,8,9]
bubble_short(a1)