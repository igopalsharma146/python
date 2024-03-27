count=0
with open("lecture 7\practice set 5.txt","r") as f:
        data=f.read()
        print(data)
        
        #we can do find the our numbers in a string by using split method.
        nums=data.split(",")
        print(nums)
        for val in nums:
            if (int(val)%2==0):
                count +=1
print(count)