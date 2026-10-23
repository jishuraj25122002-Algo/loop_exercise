n = 5
# Outer loop for number of rows (5 down to 1)
for i in range(n, 0, -1):
    # Inner loop for printing numbers in each row
    for j in range(i, 0, -1):
        print(j, end=' ')
    # New line after each row
    print("")