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
info1.pop("percentage")
info1.popitem()
del info1["is_adult"]
print(info1)