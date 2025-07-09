a=1234
rev=0
temp=a
while temp >0:
    b=temp%10
    rev=rev*10+b
    temp=temp//10
print(rev)
