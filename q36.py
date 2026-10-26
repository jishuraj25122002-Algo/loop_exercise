binary_str = "1101"
decimal_val = 0

# Reverse to handle indices as powers (0, 1, 2...)
reversed_binary = binary_str[::-1]

for i in range(len(reversed_binary)):
    if reversed_binary[i] == '1':
        decimal_val += 2 ** i

print("Decimal value:", decimal_val)