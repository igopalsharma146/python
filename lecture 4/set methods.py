# set.add()   Add an element
name=set()
print(name)
name.add(1)
name.add(2)
name.add(13)
name.add(14)
name.add(0)
name.add(2)
name.add(2)
name.add((1,2,34))
name.add("go")
name.add("hello")
name.add(22.4)
print(name)
print(len(name))

print("\n\n")
# set.remove()   Remove an element
#name.remove(7)  ->key error because value is not exists.
name.remove(2)
name.remove("hello")
name.remove(22.4)
print(name)
print("\n\n")


# set.clear()   Empities the set
name.clear()
print(name)
print(len(name))
print("\n\n")


#set.pop()      #Remove a rendom value
name=set()
print(name)
name.add(1)
name.add(2)
name.add(13)
name.add(14)
name.add(0)
name.add(2)
name.add(2)
name.add((1,2,34))
name.add("go")
name.add("hello")
name.add(22.4)
print(name)
print(len(name))
print("deleted item:",name.pop())
print("deleted item:",name.pop())
print("deleted item:",name.pop())
print(name)
print(len(name))
print("\n\n\n")


#set.union(set2)    -> Combination both set values & returns new.
set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8,9,9,10}
print(set1.union(set2))
print(set1)
print(set2)
print("\n\n")

# set.intersection(set2)  -> combines common value & returns new.
set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8,9,9,10}
print(set1.intersection(set2))
print(set1)
print(set2)
