#store folowing words meaning in python dictionary.
#table:"a piece of furniture","List of facts & figures."
# cat:"a small animal"
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","List of facts & figures."]
}
print(dictionary)
print("\n\n")

# Q:2 ->you are given a list of subjects for students, assume one classroom is required for 1 subject.how many classrooms are needed by all students.
# "python","java","c++","python","js"
# "java","python","java","C++","c"
subjects={
    "python","java","c++","python","js",
    "java","python","java","c++","c"
}
print(subjects)
print("total classrooms required:",len(subjects))
print("\n\n")


# Q:3 ->WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
x=eval(input("enter phy : "))
marks.update({"phy":x})
x=eval(input("enter chemistry : "))
marks.update({"chemistry":x})
x=eval(input("enter math : "))
marks.update({"math":x})
print(marks)
print("\n\n")


# Q:4 -> Figure out a way to store 9 & 9.0 as separate value in the set. (You can take help of built in data types)
values={9,9.0}
print(values)

values={9,"9.0"}
print(values)

#using buit in datatype
values={
    ("float",9.0),
    ("int",9)
}
print(values)