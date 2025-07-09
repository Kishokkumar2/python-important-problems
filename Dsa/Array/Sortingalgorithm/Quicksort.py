import random
def merge(a):
    if len(a) <=1:
        return a
    pivot=random.choice(a)
    left=[]
    for i in a:
        if i<pivot:
            left.append(i)
    right=[]
    for i in a:
        if i>pivot:
            right.append(i)
    middle=[]
    for i in a:
        if i==pivot:
            middle.append(i)
    return merge(left)+middle+merge(right)



















a=[5,4,3,2,1]
print("sorted",merge(a))