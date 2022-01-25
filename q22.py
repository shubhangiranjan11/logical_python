flight=[12,3,4,5,6,7,890,98,76,5,4,2,1,45,0]
min=flight[0]
sec_min=flight[0]
i=0
while i<len(flight):
    if flight[i]<min:
        min=flight[i]
    i=i+1
print(min)
index=0
while index<len(flight):
    if sec_min>flight[index]>min:
        sec_min=flight[index]
    index=index+1
print(sec_min)




