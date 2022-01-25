a=[[1,2,4],[5,1,9],[2,9,9,5]]
empty=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        empty.append(a[i][j])
        j=j+1
    i=i+1
print(empty)
k=0
while k<len(empty):
    index=0
    while index<len(empty):
        if empty[k]<empty[index]:
            empty[k],empty[index]=empty[index],empty[k]
        index+=1
    k+=1
print(empty)
