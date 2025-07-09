a = [5, 2, 9, 1, 5, 6]
n = len(a)

# Bubble sort logic
for i in range(n):
    for j in range(n - 1):  # go till second last element
        if a[j] > a[j + 1]:
            # swap if left is greater than right
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)
