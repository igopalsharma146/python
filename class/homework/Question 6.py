"""
    6) write a program to read the distance any two cities in km. and print the distance in meters,centimeter.
    """
km=eval(input("enter the distance b/w two cities in kilo meter:"))
meters=km*1000
cm=meters*100
s="Distence b/w two city in km is {0} \nIn meters is:{1} \nIn centimeter is:{2}"
print(s.format(km,meters,cm))