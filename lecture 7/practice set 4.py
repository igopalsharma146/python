""" 
1).Write a function in which line of the file does the word "learning" occur first.
print-1 if word not found.
"""
def check_for_word():
    word="learning"
    with open("lecture 7\practice set 2.txt","r") as f:
        data=f.read()
    
        if(word in data ):
            print("found")
        else:
            print("not found")
check_for_word()

def check_for_line():
    word="programming"
    data=True
    line_number=1
    with open("lecture 7\practice set 2.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_number)
                return
            line_number +=1
    return -1
print(check_for_line())


