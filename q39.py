nested_list = [[10, 20], [30, 40], [50, 60]]
flattened = []

# Iterate through each sub-list
for sublist in nested_list:
    # Iterate through each item in the current sub-list
    for item in sublist:
        flattened.append(item)

print("Flattened List:", flattened)