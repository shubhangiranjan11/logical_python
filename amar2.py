lower=int(input("any number"))
upper=int(input("any number"))
for num in range(lower,upper+1):
    temp=num
    sum=0
    while temp>0:
        rem=temp%10
        sum=sum+rem**3
        temp=temp//10
    if num==sum:
        print(num)

