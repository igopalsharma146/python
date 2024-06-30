'''
1). Create a student class that takes name and marks of three subjects as arguments in constructor.
then create a method to print the average.
'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        avg=sum/3
        print("Hello!",self.name,".","Your average score is:",avg)
s1=student("GOPAL SHARMA",[99,98,97])
s1.get_avg()
s2=student("ARMAN KHAN",[99,90,87])
s2.get_avg()
s2.name="GOPI"
s2.get_avg()
