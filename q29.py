list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
my_list=[]
for i in list_a :
  for j in list_b:
    if i == j:
      my_list.append(i)

print(f"common elements are : { my_list }")      