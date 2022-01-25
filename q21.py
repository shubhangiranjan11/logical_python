dict1={"a":29,"b":55,"c":90,"d":177,"e":123,"k":80,"y":76}
max=0
sec=0
third=0
for i in dict1:
    if dict1[i]>max:
        max=dict1[i]
print(max)
for index in dict1:
    if sec<dict1[index]<max:
        sec=dict1[index]
print(sec)
for x in dict1:
    if third<dict1[x]<sec:
        third=dict1[x]
print(third)



