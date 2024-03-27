""" 
Write a function that replace all occurences of "java" with "python" in above file.
"""
with open("lecture 7\practice set 2.txt","r") as f:
    data=f.read()
    
new_data=data.replace("java","python")
print(new_data)

with open("lecture 7\practice set 2.txt","w") as f:
    data=f.write(new_data)