var="MoNa"
i =0
while i < len(var):
    if ord(var[i])>=65 and ord(var[i]) <=90:
        b= ord(var[i])+32
        print(chr(b),end="")
    else:
        c=ord(var[i])-32
        print(chr(c),end="")
    i+=1




s="MoNa"
new=""
for i in range(len(s)):
    if s[i].isupper:
        new=new+s[i].lower()
    elif s[i].islower:
        new=new+s[i].upper()
    else:
        new=new+s[i]
print(new)


var="MoNa"
print(var.swapcase())

