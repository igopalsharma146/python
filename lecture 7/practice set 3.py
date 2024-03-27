""" 
search if the word "learning" exixt in the file or not.
"""
word="learning"
with open("lecture 7\practice set 2.txt","r") as f:
    data=f.read()
    
    if(data.find(word) != -1 ):
        print("found")
    else:
        print("not found")
    