def list(list1,ind=0):
    if(ind==len(list1)):
        return
    print(list1[ind])
    list(list1,ind+1)
fruits=["apple","mango","banana","grapes","ber","litchi"]
list(fruits)
