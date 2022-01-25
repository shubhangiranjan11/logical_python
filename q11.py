import random
flight=[1,2,3,4,5,6,7,8]
random.shuffle(flight)
count=0
empty=[]
i=0
while i<len(flight):
    if flight[i] not in empty:
        if count<5:
            empty.append(flight[i])
            count=count+1
    i=i+1
print(empty)

