#     *
#    **
#   ***
#  ****
# *****
a = int(input("Enter: "))
space=a-1
for i in range(0,a):
    for j in range(i,space):
        print(end= " ")
    for k in range(0,i+1):
        print("*",end="")
    print()


