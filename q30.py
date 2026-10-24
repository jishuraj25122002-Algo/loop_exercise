my_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list =[]
for num in my_list:
  if num not in unique_list:
    unique_list.append(num)
print(f"unique list is : { unique_list }")    