q=[[4,5,6],[7,8,9],[10,11,12]]
i=0
b=[]
while i<len(q):
    j=0
    sum=0
    while j<len(q[i]):
        sum=sum+(q[i][j])
        j=j+1
    b.append(sum)
    i=i+1
print(b)







