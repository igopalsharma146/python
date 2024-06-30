
def decoder(n):
    temp1=n[::-1]
    decoder="hdsfd"+ temp1 + "jdsgf"
    print(decoder.lower())
    
    print("\n\nPress 1 : For decode Again... ")
    print("Press Any Key : For Exit...")
    key=eval(input("\nEnter your key Answer : "))
    if(key==1):
        print(n)
    else:
        print("Program Exited...")
        exit(0)
name=input("Enter your name:")
decoder(name)

