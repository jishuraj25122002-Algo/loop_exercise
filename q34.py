# First two terms
num1, num2 = 0, 1

print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    # Calculate next term
    res = num1 + num2
    # Update values for next iteration
    num1 = num2
    num2 = res