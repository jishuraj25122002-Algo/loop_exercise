# Outer loop for rows
for i in range(1, 11):
    # Inner loop for columns
    for j in range(1, 11):
        # Print product followed by a tab for alignment
        print(i * j, end="\t")
    # Move to the next line after finishing a row
    print()