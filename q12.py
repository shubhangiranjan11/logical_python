def score(var):
    b=[]
    e=[]
    i=0
    while i<len(var):
        if var[i]%5==0:
            if var[i]>50:
                b.append(var[i])
        i=i+1
    return b
var=[5,25,55,75,45,65,75,40,25,20,10,98,78,66,79,12,13,44]
score(var)
print(score(var))


# var=[5,25,55,75,45,65,75,40,25,20,10,98,78,66,79,12,13,44]
# b=[]
# i=0
# while i<len(var):
#     if var[i]%5==0 and var[i]>50:
#         b.append(var[i])
#     i=i+1
# print(b)




