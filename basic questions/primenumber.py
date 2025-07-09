a=int(input("enter a num"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count=count+1
    else:
        pass
print("prime" if count==2 else "not")