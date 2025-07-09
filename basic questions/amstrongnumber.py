num = int(input("Enter a number: "))
order = len(str(num))  # Number of digits
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum+ digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")
