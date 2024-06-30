def selection_short(array):
    n=len(array)
    for i in range (n-1):
        min=i
        for j in range (i+1,n):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
        print("pass:",i,array)
a1=[66,7,3,45,8,9]
selection_short(a1)
