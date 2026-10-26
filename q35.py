num = 28
divisor_sum = 0

# A divisor cannot be greater than half the number
for i in range(1, (num // 2) + 1):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")