a=5
space=a-1
for i in range(0,a):
    for j in range(0,space):
        print(end= " ")
    space=space-1
    for k in range(1,i+2,2):
        print(k*"*",end= " ")
    print()

