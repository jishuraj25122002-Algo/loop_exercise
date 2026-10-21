num = 75869
# Initialize with opposite extremes
largest = 0
smallest = 9

while num > 0:
    digit = num % 10
    
    # Check for new largest
    if digit > largest:
        largest = digit
    # Check for new smallest
    if digit < smallest:
        smallest = digit
        
    num = num // 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)