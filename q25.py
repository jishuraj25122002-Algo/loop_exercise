rows = 5

# Upper part of the pattern
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\r")