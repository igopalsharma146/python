str1="my name is gopal sharma."
print(str1.endswith("ma."))
print(str1.endswith("op"))

print(str1.capitalize()) 
print(str1) #original string could not change.

a="i am from boontoli."
b=a.capitalize() #capitalize first letter
print(b)
print(a)

str2=str1.replace("my","mera") #replacing words old to new
print(str2)

#word finding
str3=str1.find("is")
print(str3)
str3=str1.find("o")
print(str3)
str3=str1.find("in")
print(str3)

#counts the occurence of substr in str
str4=str1.count("a")
print(str4)
str4=str1.count("o")
print(str4)
str4=str1.count("n")
print(str4)
str4=str1.count("opa")
print(str4)
str4=str1.count("k")
print(str4)