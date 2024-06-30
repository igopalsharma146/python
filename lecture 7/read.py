#if we are read the all data in first, then we want to print our next line . then our next line is not print because of our data in first is already readed. then in the last our code is read the \n and print the empty line .
f=open("lecture 7\demo.txt","r")
#here we reading the file
data=f.read()
print(data)
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()