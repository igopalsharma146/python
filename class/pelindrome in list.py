#palindrome list
def pelindrome(l1):
    temp=l1
    l2=[]
    for i in range (1,len(l1)+1):
        l2.append(l1[-i])
    print(l2)
    if(l2==temp):
        print("palindrome")
    else:
        print("not palindrome")
l1=[10,20,10]
pelindrome(l1)

'''#palindrome list
def pelindrome(l1):
    temp=l1 #list are mutable, here temp is the reference of l1 , when we are change the l1 then temp is also change.
    print(l1)
    l1.reverse()
    l2=l1.copy()
    print(l2)
    print(temp)
    if(l2==temp):
        print("palindrome")
    else:
        print("not palindrome")
l1=[10,20,30]
pelindrome(l1)'''

#palindrome list
def pelindrome(l1):
    temp=l1.copy()
    print(l1)
    l1.reverse()
    l2=l1.copy()
    print(l2)
    print(temp)
    if(l2==temp):
        print("palindrome")
    else:
        print("not palindrome")
l1=[10,20,10]
pelindrome(l1)