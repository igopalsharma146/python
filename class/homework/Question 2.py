"""
Q:2 -> consider a sinerio where a son eats five chocolate every weak. the price of each chocolate is different.His father pays the bill to the chocolate bender(shopkeeper) at the end of the week. Dovelop the program that generate the bill for the chocolate and sent to the father.
    """
i=1
while(i<=4):
    first=eval(input("Enter the first chocolate price:"))
    second=eval(input("Enter the second chocolate price:"))
    third=eval(input("Enter the third chocolate price:"))
    fourth=eval(input("Enter the first chocolate price:"))
    fifth=eval(input("Enter the first chocolate price:"))
    sum=first+second+third+fourth+fifth
    s="In {0} week bill of chocolate is:{1}"
    print(s.format(i,sum))
    i=i+1