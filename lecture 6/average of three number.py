#jo function return me kuch bhi return nahi karta hai. To usme automatically None value aa jati hai.
def avg(a,b,c):
    avg1=(a+b+c)/3
avg1=avg(3,4,5)
print(avg1)

def avg(a,b,c):
    avg1=(a+b+c)/3
    return avg1
avg1=avg(3,4,5)
print(avg1)