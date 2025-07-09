a=[1,1,2,2,3,4,4,5,6,6,7,8,8,10,10,1,1,11,11,11]
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)