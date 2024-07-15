#It return the largest integer value but not greater than given value

#EX:we give x=3.534,then it return the largest integer value 3,because value should not be greater than x. 
import math
x=3.534
print(math.floor(x))

# it return the -4 , because -4 is smaller then -3.3464.negetive value jitni badi hogi vo utni hi chhoti hoti hai.
x1=-3.3464
print(math.floor(x1))

x2=5.499
print(math.floor(x2))

x3=3.999
print(math.floor(x3))


#if we are write x=6.00001,then it should be return 6,because value should not be greater than x=6.99999 

x4=6.99999
print(math.floor(x4))