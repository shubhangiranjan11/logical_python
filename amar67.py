number=int(input("any number"))
power=int(input("any number"))
b=number**power
tot=0
while b>0:
    digit=b%10
    tot=tot+digit
    b=b//10
print(tot)
