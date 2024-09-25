def factorial_iterative(n):
  if n<0:
    return "Factorial not defined for negatives numbers"
    result=1
    for i in range (1,n+1):
      result*=i
     return result
num=5
print(f"Factorial of{num}(Iterative):{factorial_iterative(num)}")
