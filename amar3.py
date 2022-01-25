user=int(input("any number"))
user1=int(input("any number"))
for num in range(user,user1+1):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print(num)