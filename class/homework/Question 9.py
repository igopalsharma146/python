'''
9).Write a program to pass a list to a function.Calculate total no. of positive and negetive number.
And then display the count in term of dictionary.
'''
def calculate_positive_negative(list):
    positive,negetive=0,0
    for i in list:
        if (i>0):
            positive+=1
        elif(i<0):
            negetive+=1
    print("Total positive numbers:",positive)
    print("Total negetive numbers:",negetive)
    dict={}
    dict.update({"positive":positive})
    dict.update({"negetive":negetive})
    print(dict)
l1=[2,3,45,67,8,9,8,-76,-5,-3]
calculate_positive_negative(l1)