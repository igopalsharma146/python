# dictionary unorder hoti hai.
# isme idexing 0,1,2 isa nahi hota hai.
# list or dictionary are mutable. hum inhe change kar sakte hai. don't allow duplicate key.


info={
    "key":"value",
    "name":"gopal sharma",
    "learning":"coding",
    "cgpa":"8.77",
    "age":20,
    "is_adult":True,
    "percentage":92.20 
    #isi tarah hum python me dictinary ke ander int, float,bool,str etc. likh sakte h.
}
print(info)


# list or dictionary are mutable. hum inhe change kar sakte hai. don't allow duplicate key.
info["name"]="Gopal"
info["surname"]="sharma"
print(info)


info1={
    "name":"gopal sharma",
    "subjects":["python","java","c","c++"],
    "topics":("dics","set"),
    "cgpa":"8.77",
    "age":20,
    "is_adult":True,
    "percentage":92.20,
    2:9,
    334.9:87.7
    #isi tarah hum python me dictinary ke ander int, float,bool,str etc. likh sakte h.
}
print(info1)
print(type(info1))
print(info1["name"])
print(info1["age"])
print(info1["subjects"])
print(info1["topics"])
print(info1["is_adult"])



