# str="mona is a good girl"
# for i in range(0, len(str)):
#     if (str[i] == ' '):
#         str = str.replace(str[i], '-')
#         print(str)

str="mona is a good girl"
d=str.split()
print(d)
str="-".join(d)
print(str)



