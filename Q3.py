p=["shubhangi","rani","priya","anjali","rabiya"]
user=(input("any number="))
i=0
while i<len(p):
    j=0
    while j<len(p[i][0]):
        if user==p[i][j]:
            print(p[i]) 
        j=j+1
    i+=1

