words=["xyz","abc","aba","1221"]
i=0
c=0
while i<len(words):
    if (len(words[i])) >=2 and (words)[i][0]==(words)[i][-1]:
        c=c+1
    i=i+1
print(c)



# a=["xyz","abc","aba","1221"]
# i=0
# while i<len(a):
#     b=a[i]
#     c=len(b)-1
#     d=a[i][c]
#     e=a[i][0]
#     if (d==e):
#         print(c)
#     i=i+1
