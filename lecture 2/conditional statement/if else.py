light="green"
if(light=="red"):
    print("stop.")
elif(light=="yello"):
    print("look")
elif(light=="green"):
    print("go.")
    
    
    num=5
    if(num>=2):           #if ke ander jo bhi condition hoti hai vo her baar check hoti hai
        print("num is greater than 2.")
    if(num>=3):
        print("num is greater than 2.")
        
        num=5
    if(num>=2):           #elif ke ander jo condition hoti hai vo tabhi check hoti hai.
        print("num is greater than 2.")#jab if wali condition false hoti hai.
    elif(num>=3):
        print("num is greater than 3.")
        
light="na pato"
if(light=="red"):
    print("stop.")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("look")
else:#else wali condition ek baar check hoti hai.
    print("Light is broken.")