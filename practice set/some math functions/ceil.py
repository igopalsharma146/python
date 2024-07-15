#return the smallest integer value not smaller than given value

#EX: we give x=3.534, then it return the smallest value 4. because value should not be smaller than x. 
import math
x=3.534
print(math.ceil(x))

x1=-3.3464
print(math.ceil(x1))

x2=5.499
print(math.ceil(x2))

x3=3.999
print(math.ceil(x3))


#if we are write x=6.00001,then it should be return 7,because value should not be smaller than x=6.00001 

x4=6.00001
print(math.ceil(x4))