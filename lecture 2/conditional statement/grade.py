marks=int(input("Enter the marks:"))
if(marks>=90):
    grade="A"
    print("Grade is:",grade)
elif(marks>=75 and marks<90):
    grade="B"
    print("Grade is:",grade)
elif(marks>=60 and marks<75):
    grade="C"
    print("Grade is:",grade)
elif(marks>=40 and marks<60):
    grade="D"
    print("Grade is:",grade)
else:
    print("Fail.")