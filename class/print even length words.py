#print even word length
str="This is a python language"
str2=""
l=str.split()
for i in l:
    if len(i)%2==0 :
        str2=str2+i+" "
print(str2)