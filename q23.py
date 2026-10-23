rows = 5
ascii_value = 65 # Starting with 'A'

for i in range(rows):
    # Calculate current letter
    letter = chr(ascii_value + i)
    # Print the letter (i + 1) times
    for j in range(i + 1):
        print(letter, end=" ")
    print()