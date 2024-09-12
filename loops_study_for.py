def factorial_for(num):
  """Calculates the factorial of a number using a for loop.

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
    for i in range(1, num + 1):
      factorial *= i
    return factorial

# Get the number from the user
number = int(input("Enter a number: "))

# Calculate the factorial using a for loop
result = factorial_for(number)
print("Factorial of", number, "is", result)