#factorial program
def factorial (n):
  """this function calculates the factorial of a given number"""
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
#main program
number=int(input("enter a number:"))
if number<0:
  print("factorial is not defined for negative numbers")
else:
  result=factorial (number)
  print("the factorial of", number,"is", result)