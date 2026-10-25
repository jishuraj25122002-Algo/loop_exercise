nums = [1, 2, 3, 4, 5]
k = 2

# Perform the rotation k times
for _ in range(k):
    # Remove the first element
    first_element = nums.pop(0)
    # Move it to the end
    nums.append(first_element)

print("Rotated List:", nums)