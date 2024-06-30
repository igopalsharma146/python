def reverse_sentence(str):
    for i in range(1,len(str)):
            print(str[::-i])
n=input("Enter a sentence :")
reverse_sentence(n)