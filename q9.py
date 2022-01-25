list1=["A","B"]
user=int(input("any number"))
empty=[]
i=1
while i<=user:
    j=0
    while j<len(list1):
        empty.append(list1[j]+str(i))
        j=j+1
    i=i+1
print(empty)



