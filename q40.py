matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]
target = 30

for r_idx, row in enumerate(matrix):
    for c_idx, val in enumerate(row):
        if val == target:
            print(f"Target {target} found at Row: {r_idx}, Column: {c_idx}")
            break # Found it!