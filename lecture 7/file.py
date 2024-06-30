""" 
FILE I/O IN PYTHON:Pyhton can be use to perform operations on a file.(read & write data)

Types of all files:
1.text File : .txt , .docx , .log etc
2.Binari files: .mp4 , .mov , .png , .jpeg etc.
"""


""" 
OPEN , READ , & CLOSE FILE: we have to open a file before reading or writing.

f = open("file_name","mode")

file_name : sample.txt
            demo.docx

mode:
    r : read mode
    w : write mode
    
    
data = f.read()
f.close()

"""


""" 
FILE OPERATIONS:
'r' : open for reading (default)
'w' : open for writing,truncating the file first
'x' : create a new file and open it for writing
'a' : open for writing, appending to the end of the file if it exists.
'b' : binary mode
't' : text mode default
'+' : open a disk file for updating (reading and writing)
"""

f=open("lecture 7\demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()