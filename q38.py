n = 5
start = 2
sum_seq = 0

for i in range(0, n):
    # Add current term to the total sum
    sum_seq += start
    # Generate the next term (e.g., 2 -> 22 -> 222)
    start = start * 10 + 2

print(sum_seq)