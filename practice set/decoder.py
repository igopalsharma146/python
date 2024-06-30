def decoder(n):
    temp1=n[1:len(n)]
    temp2=n[0]
    temp3=temp1 + temp2
    decoder="hdsfd"+ temp3 + "jdsgf"
    print(decoder.lower())
name=input("Enter your name:")
decoder(name)
