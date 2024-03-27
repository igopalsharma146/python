""" 
WITH SYNTAX:with open("demo.txt","a") as f:
data=f.read()
"""
with open("lecture 7\demo5.txt","r") as f:
    data=f.read()
    print(data)
    
with open("lecture 7\demo5.txt","w") as f:
    f.write("gayi bhais pani me.")
    