student={
    "name":"gopal",
    "surname":"sharma",
    "subjects":{
        "phy":98,
        "chem":96,
        "math":100
    }
}
print("\n----------------------------------------------------------------------------\n")
print(student)
print(student["subjects"])
print(student["subjects"]["math"])

print("\n----------------------------------------------------------------------------\n")
#mydict.keys()  return all keys
print(student.keys())

print("\n----------------------------------------------------------------------------\n")
#we can do convert our key in list
print(list(student.keys()))

print("\n----------------------------------------------------------------------------\n")
#mydict.values()  return all values
print(student.values())
print(list(student.values()))

print("\n----------------------------------------------------------------------------\n")
#mydict.items()  return all (key,val) pairs as tuples.
print(student.items())
print(list(student.items()))

print("\n----------------------------------------------------------------------------\n")
#mydict.get()  return the key according to value.
print(student["name"])
print(student.get("name"))
print(list(student.get("name")))
# print(student["name2"])     ->error
print(student.get("name2"))   # no error -> None

print("\n----------------------------------------------------------------------------\n")
#mydict.update()  Insert the specified items to the dictionary.
student.update({"city":"alwar"})
print(student)

print("\n----------------------------------------------------------------------------\n")
new_dict={"roll":8,"marks":38,"name":"sharmaji"}
student.update(new_dict)
print(student)