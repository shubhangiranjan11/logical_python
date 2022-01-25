user=int(input("any number"))
tot=0
sum=0
while user>0:
    digit=user%10
    tot=(tot*10)+digit
    user=user//10
print(tot)

