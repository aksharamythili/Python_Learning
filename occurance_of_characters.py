str=input("enter your string:")
print("sting=",str)
count={}
for i in str:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
             count[i]=1
print(count)
for i in count:
    print(i,"occurs for",count[i],"times")
