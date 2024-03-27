#if we are open a file in write mode or that file is not exist then our program is automatically creat a file . then our data is write.
f=open("lecture 7\demo2.txt","w")

f.write("I want to learn javascript tomorrow.") #overlap
f.close()

f=open("lecture 7\demo2.txt","a") #append

f.write("\nthen i will move to reactJS.")
f.close()