def insertion_short(array):
    n=len(array)
    for i in range (1,n):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            array[j]=key
            j-=1
            #j-=1
            #print("pass:",i,array)
        print("pass:",i,array)
a1=[66,7,3,45,8,9]
insertion_short(a1)