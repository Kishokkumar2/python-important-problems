# *********
#  *******
#   *****
#    ***
#     *

a=int(input("enter"))
space=a-1
for i in range(0,a):
    for j in range(0,i):
        print(end= " ")
    for k in range(i,a):
        print("*",end=" ")
    print()
