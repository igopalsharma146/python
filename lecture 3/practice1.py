#wap to check if a list contains a pelindrome of elements.
list1=[3,4,44,5]
copy_list1=list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not palindrome")
    
list2=[1,2,3,2,1]
copy_list2=list2.copy()
copy_list2.reverse()
if (copy_list2 == list2):
    print("Palindrome")
else:
    print("Not palindrome")
    
list2=["m","a","a","m"]
copy_list2=list2.copy()
copy_list2.reverse()
if (copy_list2 == list2):
    print("Palindrome")
else:
    print("Not palindrome")
    
    
list2=["m","a","a","m","n"]
copy_list2=list2.copy()
copy_list2.reverse()
if (copy_list2 == list2):
    print("Palindrome")
else:
    print("Not palindrome")