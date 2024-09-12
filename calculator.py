def calculate(num1, num2, operator):
  """Performs a specified arithmetic operation on two numbers.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The arithmetic operator (+, -, *, /).

  Returns:
    The result of the calculation.
  """

  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    print("Invalid operator!")
    return None

def main():
  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculate(num1, num2, operator)

    if result is not None:
      print("Result:", result)

    continue_input = input("Do you want to continue (y/n)? ")
    if continue_input.lower() != 'y':
      break

if __name__ == "__main__":
  main()