def perform_arithmetic_operations(num1, num2):
  """Performs basic arithmetic operations and prints the results.

  Args:
    num1: The first number.
    num2: The second number.
  """

  # Addition
  addition = num1 + num2
  print("Addition:", addition)

  # Subtraction
  subtraction = num1 - num2
  print("Subtraction:", subtraction)

  # Multiplication
  multiplication = num1 * num2
  print("Multiplication:", multiplication)

  # Division
  division = num1 / num2
  print("Division:", division)

  # Floor division
  floor_division = num1 // num2
  print("Floor division:", floor_division)

  # Modulus (remainder)
  modulus = num1 % num2
  print("Modulus:", modulus)

  # Exponentiation
  exponentiation = num1 ** num2
  print("Exponentiation:", exponentiation)

# Get user input for the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to perform the operations
perform_arithmetic_operations(num1, num2)