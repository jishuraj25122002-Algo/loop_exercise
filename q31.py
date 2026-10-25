numbers = [1, 2, 3, 4, 5, 6]
evens = []
odds = []
for n in numbers:
  if n % 2 == 0:
    evens.append(n)
  else:
    odds.append(n)
result = evens + odds 
print(result )      
