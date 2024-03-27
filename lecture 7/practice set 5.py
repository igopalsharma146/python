""" 
From a file containning numbers separated by comma,print the count of even numbers.
"""
with open("lecture 7\practice set 5.txt","r") as f:
        data=f.read()
        print(data)
        
        #we can do find the our numbers in a string by using split method.
        #here we are doing this without split method.
        num=""
        for i in range(len(data)):
            if(data[i]==","):
                print(int(num))
                num=""
            else:
                num += data[i]