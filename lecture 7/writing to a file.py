""" 
f=open("demo.txt","w')
f.write("this is a new line") #over write the entire file.

f=open("demo.txt","a")
f.write("this is a new line") #add to the file
"""
f=open("lecture 7\demo1.txt","w")

f.write("I want to learn javascript tomorrow.") #overlap
f.close()

f=open("lecture 7\demo1.txt","a") #append

f.write("\nthen i will move to reactJS.")
f.close()