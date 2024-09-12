def factorial_while(num):
  """Calculates the factorial of a number using a while loop.

  Args:
    num: The number whose factorial to calculate.

  Returns:
    The factorial of the number.
  """

  if num < 0:
    return "Factorial of negative numbers is not defined."
  elif num == 0:
    return 1
  else:
    factorial = 1
    while num > 0:
      factorial *= num
      num -= 1
    return factorial

# Get the number from the user
number = int(input("Enter a number: "))

# Calculate the factorial using a while loop
result = factorial_while(number)
print("Factorial of", number, "is", result)