def merge(a):
    if len(a) <=1:
        return a
    if len(a) >1:
        middle=len(a)//2
        left=a[:middle]
        right=a[middle:]
        merge(left)
        merge(right)

    






a=[5,4,3,2,1]
print("sorted",merge(a))