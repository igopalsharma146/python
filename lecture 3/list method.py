list=[45,77,65,67]
list.append(4)
print(list)

list.reverse()
print(list)

list.sort(reverse=True)
print(list)

list.sort()
print(list)

list.insert(4,"gopal")
print(list)
list.insert(5,"sharma")
print(list)

#returning none value
list1=[54,5,52,34]
print(list1.append(4))
print(list1.sort())
print(list1)
#removing value
list1.remove(5) #remove value ko find karke delete karta hai
print(list1)

list1.pop(2) #pop operation indexing ki value ko delete kar deta hai.
print(list1)

list2=["apple","banana","lichi","grapes"]
print(list2.sort())
print(list2)

'''
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)
'''
