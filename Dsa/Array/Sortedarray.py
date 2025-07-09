a = [1, 2, 3, 4, 5, 7, 7, 10,9]

is_sorted = True
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("sorted")
else:
    print("not")
