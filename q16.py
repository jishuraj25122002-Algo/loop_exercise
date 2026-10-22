number = 121
# Store original to compare later
temp = number
reverse_num = 0

while number > 0:
    digit = number % 10
    reverse_num = (reverse_num * 10) + digit
    number = number // 10

if temp == reverse_num:
    print("Yes. Given number is palindrome number")
else:
    print("No. Given number is not palindrome")