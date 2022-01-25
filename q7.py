list1=[1,2,3,4]
user=int(input("any number"))
i=0
j=-1
while i<len(list1)-1:
    if list1[i]+list1[j]==user:
        print(i,j)
    i+=1



