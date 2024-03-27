gram=int(input("enter the value of gram: "))
kg=gram//1000
rem=gram%1000
s="{0} kg {1} grams"
print(s.format(kg,rem))