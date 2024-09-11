'''
8). Write a program to assign grades to student.Display All thegrades using keys And find the value of Amit
'''
def dict(dict,target):
    for i in dict:
        print("Value:",dict[i])
        
    for i in dict:
        if i==target:
            print(i)
            return i
    else:
        return -1
n=input("Enter target that you want to search:")
dict1={"1":"A","2":"B","3":"C","Amit":"D","6":"E"}
l1=dict(dict1,n)
if l1!=-1:
    print(f"value of {n} is:",dict1[l1])
else:
    print(f"{n} key is not exist.")