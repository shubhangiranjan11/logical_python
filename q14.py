list1=[1,2,3,4,5]
i=0
# j=1
sum=0
while i<(len(list1)-1):
    if i==0:
        sum=sum+list1[i]
    if i>0:
        sum=list1[i]+list1[i+1]
    print(sum)
    i=i+1
    # j=j+1


i=0
sum=0
while i<len(list1)-1:
    sum=list1[i]+list1[i+1]
    print(sum)
    i+=1
    