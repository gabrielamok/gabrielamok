def divide_numbers(num1, num2):
  """Divides two numbers.

  Args:
    num1: The first number.
    num2: The second number.

  Raises:
    ZeroDivisionError: If the second number is zero.

  Returns:
    The result of the division.
  """

  if num2 == 0:
    raise ZeroDivisionError("Cannot divide by zero.")
  return num1 / num2

def main():
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = divide_numbers(num1, num2)
    print("Result:", result)
  except ZeroDivisionError as e:
    print("Error:", e)

if __name__ == "__main__":
  main()