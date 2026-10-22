def factorial(n):
  if n ==0 or n==1:
    return 1
  elif n <0 :
    print("negative number can not be factorized .")
  else:
    return n*factorial(n-1)  

n=int(input("enter a number : "))  
result=factorial(n)
print(f" factorial of { n } is : {result }")