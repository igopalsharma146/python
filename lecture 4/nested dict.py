student={
    "name":"gopal sharma",
    "surname":"sharma",
    "subjects":{
        "phy":98,
        "chem":96,
        "math":100
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["math"])

#mydict.keys()  return all keys
print(student.keys())

#we can do convert our key in list
print(list(student.keys()))

#mydict.values()  return all values
print(student.values())
print(list(student.values()))

#mydict.items()  return all (key,val) pairs as tuples.
print(student.items())
print(list(student.items()))

#mydict.get()  return the key according to value.
print(student["name"])
print(student.get("name"))
print(list(student.get("name")))
# print(student["name2"])     ->error
print(student.get("name2"))   # no error -> None

#mydict.update()  Insert the specified items to the dictionary.
student.update({"city":"alwar"})
print(student)

new_dict={"roll":8,"marks":38,"name":"sharmaji"}
student.update(new_dict)
print(student)