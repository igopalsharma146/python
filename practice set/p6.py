# Create a program to count the frequency of characters.
def frequency_count(str):
    D=dict()
    for c in str:
        if c not in D:
            D[c]=1
        else:
            D[c]+=1
    return D
str=input("Enter the string :")
Output=frequency_count(str)
print(Output)