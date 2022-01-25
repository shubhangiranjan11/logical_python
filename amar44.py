user=int(input("any number"))
i=1
fac=1
sum=0
while i<=user:
    fac=fac*i
    sum=sum+fac
    i=i+1
print("factorial number",fac)
print(sum)