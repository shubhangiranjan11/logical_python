a=["sapna","shubhangi","durga","deepti","priya","pooja","rani","megha","ramaiya"]
user=(input("any letter="))
empty=[]
i=0
while i<len(a):
    if a[i][0]==user:
        empty.append(a[i])
    i=i+1
print(empty)



